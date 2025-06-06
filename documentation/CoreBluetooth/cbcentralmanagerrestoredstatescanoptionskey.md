# CBCentralManagerRestoredStateScanOptionsKey

**Framework**: Core Bluetooth  
**Kind**: var

A dictionary of peripheral scan options for use when restoring state.

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
let CBCentralManagerRestoredStateScanOptionsKey: String
```

#### Discussion

The value associated with this key is an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary). The dictionary contains all of the peripheral scan options in use by the central manager when the system terminated the app.

## See Also

- [let CBCentralManagerRestoredStatePeripheralsKey: String](cbcentralmanagerrestoredstateperipheralskey.md)
  An array of peripherals for use when restoring the state of a central manager.
- [let CBCentralManagerRestoredStateScanServicesKey: String](cbcentralmanagerrestoredstatescanserviceskey.md)
  An array of service IDs for use when restoring state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstatescanoptionskey)*