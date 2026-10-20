# SRAuthorizationStatus

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The states that model whether the user approves the app to read a particular sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum SRAuthorizationStatus
```

```c
enum SRAuthorizationStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [SRAuthorizationStatus.authorized](./srauthorizationstatus/authorized.md)
  User has granted authorization to this application
- [SRAuthorizationStatus.denied](./srauthorizationstatus/denied.md)
  User has denied authorization to this application or data collection is disabled in Settings.
- [SRAuthorizationStatus.notDetermined](./srauthorizationstatus/notdetermined.md)
  User has not yet made a choice regarding this application
### Initializers
- [init?(rawValue: Int)](./srauthorizationstatus/init%28rawvalue%29.md)
### Type Methods
- [static func requestAuthorization(for: [any SRDataSensor]) async throws](./srauthorizationstatus/requestauthorization%28for%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking user authorization
- [var authorizationStatus: SRAuthorizationStatus](./srsensorreader/authorizationstatus.md)
  The status of the user’s agreement to let the app access this reader’s sensor.
- [class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)](./srsensorreader/requestauthorization%28sensors,completion%29.md)
  Requests user permission to read one or more sensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus)*