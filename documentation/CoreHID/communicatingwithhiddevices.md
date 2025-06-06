# Communicating with human interface devices

**Framework**: Corehid

Interact with and obtain data from devices such as keyboards and mice.

#### Overview

To communicate with a human interface device (HID), you must identify and match it using a set of matching critiera. When you match the device, you become its client and can query its properties and capabilities.

> **Note**: Interacting with certain HIDs, such as keyboards, require user approval. Ensure that you grant permission to access the device to use it.

##### Locate the Device of Interest

To locate the device you’re interested in, specify a set of matching criteria using [`HIDDeviceManager.DeviceMatchingCriteria`](hiddevicemanager/devicematchingcriteria.md). The following code uses this method to discover the Magic Keyboard with Numeric Keypad `product`:

```swift
let matchingCriteria = HIDDeviceManager.DeviceMatchingCriteria(primaryUsage: .genericDesktop(.keyboard), product: "Magic Keyboard with Numeric Keypad")
```

Create a [`HIDDeviceManager`](hiddevicemanager.md) and provide the criteria to [`monitorNotifications(matchingCriteria:)`](hiddevicemanager/monitornotifications(matchingcriteria:).md). Notifications arrive immediately for connected devices, and later when newly connected matching devices appear. `monitorNotifications` returns an asynchronous stream that you iterate over. The loop awaits and releases the current Task until a notification comes in.

```swift
let manager = HIDDeviceManager()

// The criteria combines multiple sets in a single array.
for try await notification in await manager.monitorNotifications(matchingCriteria: [matchingCriteria]) {
    switch notification {
        case .deviceMatched(let deviceReference):
            print("A device was found.")

        case .deviceRemoved(let deviceReference):
            print("A device was removed.")

        default:
            continue
    }
}
```

To specify matching criteria using additional properties, see [`init(primaryUsage:deviceUsages:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:isBuiltIn:extraProperties:)`](hiddevicemanager/devicematchingcriteria/init(primaryusage:deviceusages:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:isbuiltin:extraproperties:).md).

##### Communicate with the Device

Create a [`HIDDeviceClient`](hiddeviceclient.md) and pass in the device reference to start communication with the device. Verify that you’re communicating with the correct device by checking the usage with [`primaryUsage`](hiddeviceclient/primaryusage.md), the transport with [`transport`](hiddeviceclient/transport.md), and the product name with [`product`](hiddeviceclient/product.md).

```swift
enum ExampleError : Error {
    case deviceCreation
    case wrongUsage
    case wrongTransport
    case wrongProduct
    case noElement
    case noValue
    case valuesNotEqual
}

guard let client = HIDDeviceClient(deviceReference: deviceReference) else {
    throw ExampleError.deviceCreation
}

let usage = await client.primaryUsage
guard usage == .genericDesktop(.keyboard) else {
    print("Wrong usage: \(usage)")
    throw ExampleError.wrongUsage
}

let transport = await client.transport
guard transport == .bluetooth else {
    print("Wrong transport: \(String(describing: transport))")
    throw ExampleError.wrongTransport
}

let product = await client.product
guard product == "Magic Keyboard with Numeric Keypad" else {
    print("Wrong product: \(String(describing: product))")
    throw ExampleError.wrongProduct
}
```

Obtain the device’s input report using [`dispatchGetReportRequest(type:id:timeout:)`](hiddeviceclient/dispatchgetreportrequest(type:id:timeout:).md). Specify [`HIDReportType.input`](hidreporttype/input.md) for the type, and provide the appropriate [`HIDReportID`](hidreportid.md). This method initiates a get report request to the device over Bluetooth and returns the device’s response.

```swift
let report = try await client.dispatchGetReportRequest(type: .input, id: HIDReportID(rawValue: 1))
print("Get report data: [\(report.map { String(format: "%02x", $0) }.joined(separator: " "))]")
```

Monitor the device for input reports or other notifications by calling [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md):

```swift
for try await notification in await client.monitorNotifications(reportIDsToMonitor: [HIDReportID.allReports], elementsToMonitor: []) {
    switch notification {

    // Receive device input data.
    case .inputReport(let reportID, let reportData, let timestamp):
        print("Received input report ID:\(String(describing: reportID)) timestamp:\(timestamp) data:[\(reportData.map { String(format: "%02x", $0) }.joined(separator: " "))]")

    // Receive a notification if another client seizes this device.
    case .deviceSeized:
        print("\(client) seized")

    // Receive a notification if another client releases this device.
    case .deviceUnseized:
        print("\(client) unseized")

    // Receive a notification if a person removes the client.
    case .deviceRemoved:
        print("\(client) removed")

    default:
        continue
    }
}
```

Raw reports provide detailed information about data going to and from the device; however, this can generate more detail than you need. Instead, use [`HIDElement`](hidelement.md) to obtain specific information from a device.

For the keyboard in this example, the input report contains the report ID, status of the modifier keys, the currently pressed keys, vendor defined data and padding. To obtain just the state of the Shift key, obtain the corresponding element.

```swift
let elements = await client.elements
guard let leftShiftKey = elements.filter({ $0.usage == .keyboardOrKeypad(.keyboardLeftShift) }).first else {
    throw ExampleError.noElement
}
```

With `leftShiftKey`, monitor [`HIDDeviceClient.Notification.elementUpdates(values:)`](hiddeviceclient/notification/elementupdates(values:).md) for any changes using [`HIDElement.Value`](hidelement/value.md). Values also arrive as a byte stream in [`bytes`](hidelement/value/bytes.md), but are interpretable as integers using extensions such as [`integerValue(asTypeTruncatingIfNeeded:)`](hidelement/value/integervalue(astypetruncatingifneeded:).md). Because the Shift key state is 1 bit, treat it as a `UInt8`.

```swift
for try await notification in await client.monitorNotifications(reportIDsToMonitor: [], elementsToMonitor: [leftShiftKey]) {
    switch notification {
    case .elementUpdates(let values):
        let leftShiftVal = values[0]
        print("Left shift state: \(leftShiftVal.integerValue(asTypeTruncatingIfNeeded: UInt8.self))")

    default:
        continue
    }
}
```

Use [`HIDElement`](hidelement.md) with get and set reports through [`updateElements(_:timeout:)`](hiddeviceclient/updateelements(_:timeout:).md). This takes [`HIDElement`](hidelement.md) from [`HIDDeviceClient.RequestElementUpdate`](hiddeviceclient/requestelementupdate.md) and [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md), then issues get and set reports with the raw report data in the background.

The following example creates a unit test for the keyboard. It turns off the Caps Lock LED, queries the state of the left Shift key, turns on the Caps Lock LED, then queries the state of the left Shift key again to determine if toggling the LED alters the state of the left Shift key.

```swift
guard let capsLockLED = elements.filter({ $0.usage == .led(.capsLock) }).first else {
    throw ExampleError.noElement
}

let turnOffVal = HIDElement.Value(element: capsLockLED, fromIntegerTruncatingIfNeeded: 0, timestamp: SuspendingClock.now)
let turnOnVal  = HIDElement.Value(element: capsLockLED, fromIntegerTruncatingIfNeeded: 1, timestamp: SuspendingClock.now)

let turnOffRequest     = HIDDeviceClient.ProvideElementUpdate(values:   [turnOffVal])
let stateRequestBefore = HIDDeviceClient.RequestElementUpdate(elements: [leftShiftKey])
let turnOnRequest      = HIDDeviceClient.ProvideElementUpdate(values:   [turnOnVal])
let stateRequestAfter  = HIDDeviceClient.RequestElementUpdate(elements: [leftShiftKey])
let requestResults     = await client.updateElements([turnOffRequest, stateRequestBefore, turnOnRequest, stateRequestAfter])

// Ensure that the set operations succeed.
try requestResults[turnOffRequest]!.get()
try requestResults[turnOnRequest]!.get()

// Read the initial state of the left Shift key.
guard let leftShiftStateBefore = try requestResults[stateRequestBefore]?.get().first?.integerValue(asTypeTruncatingIfNeeded: UInt8.self) else {
    throw ExampleError.noValue
}

// Read the final state of the left Shift key.
guard let leftShiftStateAfter = try requestResults[stateRequestAfter]?.get().first?.integerValue(asTypeTruncatingIfNeeded: UInt8.self) else {
    throw ExampleError.noValue
}

// Ensure the initial state didn't change as a result of the LED toggle.
guard leftShiftStateBefore == leftShiftStateAfter else {
    throw ExampleError.valuesNotEqual
}
```

## See Also

- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDUsage](hidusage.md)
  A type to represent HID usage pages.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreHID/communicatingwithhiddevices)*