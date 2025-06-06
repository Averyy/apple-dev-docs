# CBPeripheralManagerOptionShowPowerAlertKey

**Framework**: Core Bluetooth  
**Kind**: var

A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBPeripheralManagerOptionShowPowerAlertKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). If the key isn’t specified, the default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [let CBPeripheralManagerOptionRestoreIdentifierKey: String](cbperipheralmanageroptionrestoreidentifierkey.md)
  A unique identifier (UID) with which to instantiate the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionshowpoweralertkey)*