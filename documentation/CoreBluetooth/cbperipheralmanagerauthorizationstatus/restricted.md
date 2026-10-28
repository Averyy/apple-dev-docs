# CBPeripheralManagerAuthorizationStatus.restricted

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

An authorization status that indicates this app isn’t authorized to share data using Bluetooth while in the background.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use CBManagerAuthorization instead

## Declaration

```swift
case restricted
```

```c
CBPeripheralManagerAuthorizationStatusRestricted
```

## Discussion

The user can’t change this app’s status, possibly due to active restrictions such as parental controls being in place.

## See Also

### Constants
- [CBPeripheralManagerAuthorizationStatus.notDetermined](./notdetermined.md)
  An authorization status that indicates the user hasn’t indicated whether this app can share data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.denied](./denied.md)
  An authorization status that indicates the user explicitly denied this app from sharing data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.authorized](./authorized.md)
  An authorization status that indicates the user authorized this app to share data using Bluetooth while in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/restricted)*