# Measuring distance between devices using Channel Sounding

**Framework**: Core Bluetooth

Measure the distance between two Bluetooth Low Energy devices in real time with Channel Sounding.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample app demonstrates how to use the Channel Sounding API to continuously measure the physical distance between an iOS device and any Bluetooth Low Energy peripheral that supports Bluetooth 6.3 and Channel Sounding. The app uses [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) to pair the peripheral, [`Core Bluetooth`](CoreBluetooth.md) to establish the *ACL connection* (the standard Bluetooth data link between devices), and then starts a Channel Sounding session as the initiator to stream live distance estimates to the screen. The app supports two measurement paths: Core Bluetooth and Nearby Interaction.

The app walks through each stage of the workflow: accessory pairing via [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit), ACL connection, Channel Sounding session start, and measurement display. It keeps a rolling history of up to 200 distance readings so you can observe how distance estimates change over time.

> **Note**: This sample code project is associated with WWDC26 session 369: [`Find your accessory with Bluetooth Channel Sounding`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/369/).

#### Configure the Sample Code Project

Before running the sample code project in Xcode:

- Use an iOS 27 device with Channel Sounding-capable hardware (iPhone 17 or later) as the initiator. Channel Sounding isn’t available in Simulator.
- Use a Bluetooth Low Energy peripheral that supports Bluetooth 6.3 and Channel Sounding as the responder. The responder can be any compatible BLE device.
- Ensure your information property list includes the required [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) entries for the Bluetooth identifiers your peripheral uses.

#### Add and Pair the Accessory Using Accessorysetupkit

[`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) is the required pairing mechanism for Channel Sounding. It presents a system-managed picker that lets a person select and pair the peripheral, while keeping Bluetooth identifiers private from the app until the person explicitly grants access. Importantly, the system restricts Channel Sounding sessions to [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit)-paired devices. The system denies an attempt to start a session with a peripheral that wasn’t paired through [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit).

`BluetoothManager` activates an instance of [`ASAccessorySession`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessorySession) during its initialization and registers a closure to receive all [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) events:

```swift
override init() {
    super.init()
    askSession.activate(on: .main) { [weak self] event in
        self?.handleAccessoryEvent(event)
    }
}
```

When the person taps Add Accessory, the app presents the picker. An [`ASDiscoveryDescriptor`](https://developer.apple.com/documentation/AccessorySetupKit/ASDiscoveryDescriptor) tells [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) which Bluetooth identifiers to filter for, so only matching peripherals appear as candidates. If the person already paired the peripheral in a previous session, the app skips the picker and reconnects directly:

```swift
func showAccessoryPicker() {
    guard isSessionActivated else { return }

    if let accessory = askSession.accessories.first,
       let identifier = accessory.bluetoothIdentifier {
        connectAccessory(identifier: identifier, name: accessory.displayName)
        return
    }

    let descriptor = ASDiscoveryDescriptor()
    descriptor.bluetoothServiceUUID = Self.accessoryServiceUUIDs.first
    descriptor.supportedOptions = .bluetoothPairingLE

    let item = ASPickerDisplayItem(
        name: "BLE Peripheral",
        productImage: UIImage(systemName: "antenna.radiowaves.left.and.right") ?? UIImage(),
        descriptor: descriptor)

    askSession.showPicker(for: [item]) { error in
        if let error { print("[ASK] showPicker error: \(error)") }
    }
}
```

The app reads the discovery identifiers from the information property list.

```swift
private static let accessoryServiceUUIDs: [CBUUID] = {
    let strings = Bundle.main.infoDictionary?["NSAccessorySetupBluetoothServices"] as? [String] ?? []
    return strings.map { CBUUID(string: $0) }
}()
```

The event handler responds to two key events. On `.activated`, which fires every app launch, the handler checks whether a peripheral is already paired and reconnects automatically. On `.accessoryAdded`, which fires after the user completes the picker for the first time, it initiates a Core Bluetooth connection:

```swift
private func handleAccessoryEvent(_ event: ASAccessoryEvent) {
    switch event.eventType {
    case .activated:
        isSessionActivated = true
        if let accessory = askSession.accessories.first,
           let identifier = accessory.bluetoothIdentifier {
            connectAccessory(identifier: identifier, name: accessory.displayName)
        }
    case .accessoryAdded:
        guard let accessory = event.accessory,
              let identifier = accessory.bluetoothIdentifier else { return }
        connectAccessory(identifier: identifier, name: accessory.displayName)
    default:
        break
    }
}
```

#### Connect the Peripheral Using Core Bluetooth

After [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) provides the peripheral’s `bluetoothIdentifier`, the app initializes [`CBCentralManager`](cbcentralmanager.md), instead of at app launch. Initializing a [`CBCentralManager`](cbcentralmanager.md) before [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) completes pairing triggers the system Bluetooth permission prompt, which prevents the [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) picker from appearing.

Because the central manager may still be powering on when the app calls `connectAccessory`, the app stores the identifier and defers the actual connection until [`centralManagerDidUpdateState(_:)`](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md) fires:

```swift
private func connectAccessory(identifier: UUID, name: String) {
    if central == nil {
        central = CBCentralManager(delegate: self, queue: .main)
    }
    if central?.state == .poweredOn {
        retrieveAndConnect(identifier: identifier, name: name)
    } else {
        pendingPeripheralIdentifier = identifier
        pendingPeripheralName = name
        connectionState = .connecting(name)
    }
}
```

On the first launch after pairing, Core Bluetooth’s cache is empty, so `retrieveAndConnect` scans by service UUID and connects when [`centralManager(_:didDiscover:advertisementData:rssi:)`](cbcentralmanagerdelegate/centralmanager(_:diddiscover:advertisementdata:rssi:).md) finds a peripheral with a matching identifier. On subsequent launches, the peripheral is already in the cache, so the app uses [`retrievePeripherals(withIdentifiers:)`](cbcentralmanager/retrieveperipherals(withidentifiers:).md) to fetch it directly without scanning:

```swift
private func retrieveAndConnect(identifier: UUID, name: String) {
    let peripherals = central?.retrievePeripherals(withIdentifiers: [identifier]) ?? []
    if let peripheral = peripherals.first {
        connectedPeripheral = peripheral
        peripheral.delegate = self
        connectionState = .connecting(name)
        central?.connect(peripheral)
        return
    }
    pendingPeripheralIdentifier = identifier
    pendingPeripheralName = name
    central?.scanForPeripherals(withServices: Self.accessoryServiceUUIDs)
}
```

The app stores a strong reference to the peripheral in `connectedPeripheral` before calling `connect`, keeping the object alive until the connection completes.

#### Start a Channel Sounding Session

The app supports two measurement paths, selectable with a segmented control:

```swift
enum ChannelSoundingMethod {
    case coreBluetooth
    case nearbyInteraction
}
```

The Core Bluetooth path delivers only the distance. The Nearby Interaction path adds a horizontal angle value when camera assistance is available, enabling the directional arrow in the UI.

Calling `startChannelSounding()` clears previous readings and dispatches to the appropriate path:

```swift
func startChannelSounding() {
    guard let peripheral = connectedPeripheral, connectionState.isConnected else { return }
    guard !connectionState.isRanging else { return }
    rangeReadings.removeAll()
    currentRange = nil
    sessionError = nil

    if channelSoundingMethod == .nearbyInteraction {
        startChannelSoundingThroughNearbyInteraction(peripheral: peripheral)
    } else {
        startChannelSoundingThroughCoreBluetooth(peripheral: peripheral)
    }

    if case .connected(let name) = connectionState {
        connectionState = .ranging(name)
    }
}
```

In the Core Bluetooth path, before creating the session configuration, the app verifies that the local device hardware supports Channel Sounding. Call [`supports(_:)`](cbcentralmanager/supports(_:).md) only after a [`CBCentralManager`](cbcentralmanager.md) instance initializes and reaches the `.poweredOn` state; calling it earlier returns incorrect results. By this point in the flow, the central manager is guaranteed to be `.poweredOn` because the person has already completed pairing and connecting:

```swift
func startChannelSoundingThroughCoreBluetooth(peripheral: CBPeripheral) {
    if #available(iOS 27.0, *) {
        guard CBCentralManager.supports(.channelSounding) else {
            sessionError = "Channel Sounding is not supported on this device"
            return
        }
        let config = CBChannelSoundingSessionConfiguration(role: .initiator)
        peripheral.startChannelSoundingSession(config)
    }
}
```

In the Nearby Interaction path, the app uses [`NISession`](https://developer.apple.com/documentation/NearbyInteraction/NISession) to verify Bluetooth Channel Sounding support before starting the session:

```swift
func startChannelSoundingThroughNearbyInteraction(peripheral: CBPeripheral) {
    if #available(iOS 27.0, *) {
        guard NISession.deviceCapabilities.supportsBluetoothChannelSounding else {
            return
        }
        let config = NINearbyAccessoryConfiguration(
            bluetoothChannelSoundingIdentifier: peripheral.identifier,
            previousBluetoothIdentifier: nil)
        config.isCameraAssistanceEnabled = true
        let session = NISession()
        session.delegate = self
        session.run(config)
        niSession = session
    }
}
```

#### Process Incoming Distance Measurements

A small extension on [`CBChannelSoundingProcedureResults`](cbchannelsoundingprocedureresults.md) maps the raw `distance` property to an optional. The API returns a negative sentinel value when no valid measurement is available; the extension ensures the rest of the app only handles real readings:

```swift
extension CBChannelSoundingProcedureResults {
    var rangeValue: Double? { distance > 0 ? distance : nil }
}
```

In the Core Bluetooth path, the distance data arrives in the [`CBPeripheralDelegate`](cbperipheraldelegate.md) callback:

```swift
func peripheral(_ peripheral: CBPeripheral,
                didReceive results: CBChannelSoundingProcedureResults?,
                error: Error?) {
    guard let distance = results?.rangeValue else { return }
    currentRange = distance
    rangeReadings.append(RangeReading(meters: distance))
    if rangeReadings.count > 200 { rangeReadings.removeFirst(100) }
}
```

In the Nearby Interaction path, distance and directional data arrive via [`NINearbyObject`](https://developer.apple.com/documentation/NearbyInteraction/NINearbyObject) in the [`NISessionDelegate`](https://developer.apple.com/documentation/NearbyInteraction/NISessionDelegate) callback. In addition to distance, the Nearby Interaction path provides a horizontal angle in radians when camera assistance is available, which the `ArrowView` uses to point toward the remote device:

```swift
func session(_ session: NISession, didUpdate nearbyObjects: [NINearbyObject]) {
    guard let object = nearbyObjects.last else { return }
    if let distance = object.distance {
        currentRange = Double(distance)
        rangeReadings.append(RangeReading(meters: Double(distance)))
        if rangeReadings.count > 200 { rangeReadings.removeFirst(100) }
    }
    if let angle = object.horizontalAngle {
        currentHorizontalAngle = angle
    }
}
```

The `DistanceCard` view displays the live distance and, when the Nearby Interaction path is active, shows the `ArrowView` rotated by the horizontal angle:

```swift
if bluetooth.channelSoundingMethod == .nearbyInteraction,
   let angle = bluetooth.currentHorizontalAngle {
    ArrowView(horizontalAngle: angle)
}
```

#### Stop the Session and Clean Up

When it’s time to stop the session, `stopChannelSounding()` delegates to the active path and transitions the connection state back to `.connected`:

```swift
func stopChannelSounding() {
    guard let peripheral = connectedPeripheral else { return }

    if channelSoundingMethod == .nearbyInteraction {
        stopChannelSoundingThroughNearbyInteraction(peripheral: peripheral)
    } else {
        stopChannelSoundingThroughCoreBluetooth(peripheral: peripheral)
    }

    if case .ranging(let name) = connectionState {
        connectionState = .connected(name)
    }
}
```

For the Core Bluetooth path, [`cancelChannelSoundingSession()`](cbperipheral/cancelchannelsoundingsession().md) ends the Channel Sounding procedure on the peripheral. The [`peripheral(_:didCompleteChannelSoundingSession:)`](cbperipheraldelegate/peripheral(_:didcompletechannelsoundingsession:).md) delegate callback confirms the session ended:

```swift
func stopChannelSoundingThroughCoreBluetooth(peripheral: CBPeripheral) {
    if #available(iOS 27.0, *) {
        peripheral.cancelChannelSoundingSession()
    }
}
```

```swift
func peripheral(_ peripheral: CBPeripheral,
                didCompleteChannelSoundingSession error: Error?) {
    if case .ranging(let name) = connectionState {
        connectionState = .connected(name)
    }
    if let error { sessionError = error.localizedDescription }
}
```

For the Nearby Interaction path, [`NISession`](https://developer.apple.com/documentation/NearbyInteraction/NISession) tears down the [`NISession`](https://developer.apple.com/documentation/NearbyInteraction/NISession). The [`NISessionDelegate`](https://developer.apple.com/documentation/NearbyInteraction/NISessionDelegate) callback clears `currentRange` and `currentHorizontalAngle` from the UI:

```swift
func stopChannelSoundingThroughNearbyInteraction(peripheral: CBPeripheral) {
    if #available(iOS 27.0, *) {
        niSession?.invalidate()
    }
}
```

```swift
func session(_ session: NISession, didInvalidateWith error: any Error) {
    currentRange = nil
    currentHorizontalAngle = nil
}
```

Tapping Disconnect calls `disconnect()`, which cancels the ACL connection. The [`centralManager(_:didDisconnectPeripheral:error:)`](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:).md) callback then clears all connection state and resets the UI to `idle`.

```swift
func disconnect() {
    guard let peripheral = connectedPeripheral else { return }
    if connectionState.isRanging { stopChannelSounding() }
    central?.cancelPeripheralConnection(peripheral)
}
```

```swift
func centralManager(_ central: CBCentralManager,
                    didDisconnectPeripheral peripheral: CBPeripheral,
                    error: Error?) {
    connectedPeripheral = nil
    currentRange = nil
    currentHorizontalAngle = nil
    connectionState = .idle
}
```

## See Also

- [class CBChannelSoundingProcedureResults](cbchannelsoundingprocedureresults.md)
- [class CBChannelSoundingSessionConfiguration](cbchannelsoundingsessionconfiguration.md)
- [let CBUUIDCharacteristicObservationScheduleString: String](cbuuidcharacteristicobservationschedulestring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding)*