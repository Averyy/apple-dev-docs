# CBPeripheralManagerAuthorizationStatus

**Framework**: Core Bluetooth  
**Kind**: enum

Values representing the current authorization state of the peripheral manager.

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
enum CBPeripheralManagerAuthorizationStatus
```

## Topics

### Constants
- [CBPeripheralManagerAuthorizationStatus.notDetermined](cbperipheralmanagerauthorizationstatus/notdetermined.md)
  An authorization status that indicates the user hasn’t indicated whether this app can share data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.restricted](cbperipheralmanagerauthorizationstatus/restricted.md)
  An authorization status that indicates this app isn’t authorized to share data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.denied](cbperipheralmanagerauthorizationstatus/denied.md)
  An authorization status that indicates the user explicitly denied this app from sharing data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.authorized](cbperipheralmanagerauthorizationstatus/authorized.md)
  An authorization status that indicates the user authorized this app to share data using Bluetooth while in the background.
### Initializers
- [init?(rawValue: Int)](cbperipheralmanagerauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus](cbperipheralmanager/authorizationstatus.md)
  Returns the app’s authorization status for sharing data while in the background.
- [enum CBPeripheralManagerState](cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)*