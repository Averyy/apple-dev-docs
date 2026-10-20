# CBPeripheralManagerAuthorizationStatus

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

Values representing the current authorization state of the peripheral manager.

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
enum CBPeripheralManagerAuthorizationStatus
```

```c
enum CBPeripheralManagerAuthorizationStatus : NSInteger;
```

## Topics

### Constants
- [CBPeripheralManagerAuthorizationStatus.notDetermined](./cbperipheralmanagerauthorizationstatus/notdetermined.md)
  An authorization status that indicates the user hasn’t indicated whether this app can share data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.restricted](./cbperipheralmanagerauthorizationstatus/restricted.md)
  An authorization status that indicates this app isn’t authorized to share data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.denied](./cbperipheralmanagerauthorizationstatus/denied.md)
  An authorization status that indicates the user explicitly denied this app from sharing data using Bluetooth while in the background.
- [CBPeripheralManagerAuthorizationStatus.authorized](./cbperipheralmanagerauthorizationstatus/authorized.md)
  An authorization status that indicates the user authorized this app to share data using Bluetooth while in the background.
### Initializers
- [init?(rawValue: Int)](./cbperipheralmanagerauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Monitoring the State of a Peripheral Manager
- [class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus](./cbperipheralmanager/authorizationstatus%28%29.md)
  Returns the app’s authorization status for sharing data while in the background.
- [enum CBPeripheralManagerState](./cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)*