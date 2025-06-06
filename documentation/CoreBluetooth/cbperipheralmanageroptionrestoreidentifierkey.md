# CBPeripheralManagerOptionRestoreIdentifierKey

**Framework**: Core Bluetooth  
**Kind**: var

A unique identifier (UID) with which to instantiate the peripheral manager.

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
let CBPeripheralManagerOptionRestoreIdentifierKey: String
```

#### Discussion

The value associated with this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString).

The system uses this UID to identify a specific peripheral manager. As a result, the UID must remain the same for subsequent executions of the app for successful restoration of the peripheral manager.

## See Also

- [let CBPeripheralManagerOptionShowPowerAlertKey: String](cbperipheralmanageroptionshowpoweralertkey.md)
  A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionrestoreidentifierkey)*