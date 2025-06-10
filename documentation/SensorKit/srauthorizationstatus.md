# SRAuthorizationStatus

**Framework**: SensorKit  
**Kind**: enum

The states that model whether the user approves the app to read a particular sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum SRAuthorizationStatus
```

## Topics

### Enumeration Cases
- [SRAuthorizationStatus.authorized](srauthorizationstatus/authorized.md)
  User has granted authorization to this application
- [SRAuthorizationStatus.denied](srauthorizationstatus/denied.md)
  User has denied authorization to this application or data collection is disabled in Settings.
- [SRAuthorizationStatus.notDetermined](srauthorizationstatus/notdetermined.md)
  User has not yet made a choice regarding this application
### Initializers
- [init?(rawValue: Int)](srauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var authorizationStatus: SRAuthorizationStatus](srsensorreader/authorizationstatus.md)
  The status of the user’s agreement to let the app access this reader’s sensor.
- [class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)](srsensorreader/requestauthorization(sensors:completion:).md)
  Requests user permission to read one or more sensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srauthorizationstatus)*