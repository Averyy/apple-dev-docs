# pairedDeviceIdentifiers()

**Framework**: Accessibility  
**Kind**: method

Returns the UUIDs of the hearing device peripherals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func pairedDeviceIdentifiers() -> [UUID]
```

#### Return Value

An array of [`NSUUID`](https://developer.apple.com/documentation/Foundation/NSUUID) objects that represent the [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) UUIDs of the hearing device peripherals.

#### Discussion

This function returns each [`CBPeripheral`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheral) with a manufacturer that matches the manufacturer in your app’s `hearing.aid.app` entitlement. For bimodal hearing devices, specify an array of manufacturers for this entitlement.

Find and connect to the matching hearing device peripherals like this:

```swift
let uuids = AXMFiHearingDevice.pairedDeviceIdentifiers()
let peripherals = bluetoothManager.retrievePeripherals(withIdentifiers: uuids)
for peripheral in peripherals where peripheral.state == .connected {
    bluetoothManager.connect(peripheral)
}
```

## See Also

- [static let pairedUUIDsDidChangeNotification: NSNotification.Name](axmfihearingdevice/paireduuidsdidchangenotification.md)
  A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/paireddeviceidentifiers())*