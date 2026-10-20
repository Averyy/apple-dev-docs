# SAAuthorizationStatus

**Framework**: SafetyKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the current Crash Detection event authorization state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
enum SAAuthorizationStatus
```

```c
enum SAAuthorizationStatus : NSInteger;
```

#### Overview

To verify that your app receives Crash Detection events, call [`requestAuthorization(completionHandler:)`](./sacrashdetectionmanager/requestauthorization%28completionhandler%29.md) and inspect the authorization state.

## Topics

### Obtaining status
- [SAAuthorizationStatus.authorized](./saauthorizationstatus/authorized.md)
  This is the designated app for receiving Crash Detection events.
- [SAAuthorizationStatus.denied](./saauthorizationstatus/denied.md)
  The system denies the app from receiving Crash Detection events because another app has authorization.
- [SAAuthorizationStatus.notDetermined](./saauthorizationstatus/notdetermined.md)
  There isn’t a designated app for receiving Crash Detection events.
### Initializers
- [init?(rawValue: Int)](./saauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Detecting a crash
- [class SACrashDetectionManager](./sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [class SACrashDetectionEvent](./sacrashdetectionevent.md)
  Describes the information about a vehicular crash.
- [protocol SACrashDetectionDelegate](./sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saauthorizationstatus)*