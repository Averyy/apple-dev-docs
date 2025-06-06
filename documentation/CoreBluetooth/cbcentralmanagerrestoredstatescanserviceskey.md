# CBCentralManagerRestoredStateScanServicesKey

**Framework**: Core Bluetooth  
**Kind**: var

An array of service IDs for use when restoring state.

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
let CBCentralManagerRestoredStateScanServicesKey: String
```

#### Discussion

The value associated with this key is an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of service UUIDs (represented by [`CBUUID`](cbuuid.md) objects) containing all the services the central manager was scanning for at the time the system terminated the app.

## See Also

- [let CBCentralManagerRestoredStatePeripheralsKey: String](cbcentralmanagerrestoredstateperipheralskey.md)
  An array of peripherals for use when restoring the state of a central manager.
- [let CBCentralManagerRestoredStateScanOptionsKey: String](cbcentralmanagerrestoredstatescanoptionskey.md)
  A dictionary of peripheral scan options for use when restoring state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstatescanserviceskey)*