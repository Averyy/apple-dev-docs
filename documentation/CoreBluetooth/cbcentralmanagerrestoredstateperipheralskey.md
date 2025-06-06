# CBCentralManagerRestoredStatePeripheralsKey

**Framework**: Core Bluetooth  
**Kind**: var

An array of peripherals for use when restoring the state of a central manager.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBCentralManagerRestoredStatePeripheralsKey: String
```

#### Discussion

The value associated with this key is an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of [`CBPeripheral`](cbperipheral.md) objects. The array contains all of the peripherals connected to the central manager (or had a pending connection) at the time the system terminated the app.

When possible, the system restores all information about a peripheral, including any discovered services, characteristics, characteristic descriptors, and characteristic notification states.

## See Also

- [let CBCentralManagerRestoredStateScanServicesKey: String](cbcentralmanagerrestoredstatescanserviceskey.md)
  An array of service IDs for use when restoring state.
- [let CBCentralManagerRestoredStateScanOptionsKey: String](cbcentralmanagerrestoredstatescanoptionskey.md)
  A dictionary of peripheral scan options for use when restoring state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstateperipheralskey)*