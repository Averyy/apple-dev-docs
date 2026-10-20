# pairedDeviceIdentifiers()

**Framework**: Accessibility  
**Kind**: method  
**Role**: Type Method

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

```c
extern NSArray<NSUUID *> *AXMFiHearingDevicePairedUUIDs();
```

#### Return Value

An array of [`NSUUID`](../../Foundation/nsuuid.md) objects that represent the [Core Bluetooth](../../CoreBluetooth/CoreBluetooth.md) UUIDs of the hearing device peripherals.

#### Discussion

This function returns each [`CBPeripheral`](../../CoreBluetooth/cbperipheral.md) with a manufacturer that matches the manufacturer in your app’s `hearing.aid.app` entitlement. For bimodal hearing devices, specify an array of manufacturers for this entitlement.

Find and connect to the matching hearing device peripherals like this:

```swift
let uuids = AXMFiHearingDevice.pairedDeviceIdentifiers()
let peripherals = bluetoothManager.retrievePeripherals(withIdentifiers: uuids)
for peripheral in peripherals where peripheral.state == .connected {
    bluetoothManager.connect(peripheral)
}
```

## See Also

### Paired hearing devices
- [static let pairedUUIDsDidChangeNotification: NSNotification.Name](./paireduuidsdidchangenotification.md)
  A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/paireddeviceidentifiers())*