# SAAuthorizationStatus

**Framework**: SafetyKit  
**Kind**: enum

An enumeration that represents the current Crash Detection event authorization state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
enum SAAuthorizationStatus
```

#### Overview

To verify that your app receives Crash Detection events, call [`requestAuthorization(completionHandler:)`](sacrashdetectionmanager/requestauthorization(completionhandler:).md) and inspect the authorization state.

## Topics

### Obtaining status
- [SAAuthorizationStatus.authorized](saauthorizationstatus/authorized.md)
  This is the designated app for receiving Crash Detection events.
- [SAAuthorizationStatus.denied](saauthorizationstatus/denied.md)
  The system denies the app from receiving Crash Detection events because another app has authorization.
- [SAAuthorizationStatus.notDetermined](saauthorizationstatus/notdetermined.md)
  There isn’t a designated app for receiving Crash Detection events.
### Initializers
- [init?(rawValue: Int)](saauthorizationstatus/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](saauthorizationstatus/equatable-implementations.md)
- [RawRepresentable Implementations](saauthorizationstatus/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SACrashDetectionManager](sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [class SACrashDetectionEvent](sacrashdetectionevent.md)
  Describes the information about a vehicular crash.
- [protocol SACrashDetectionDelegate](sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saauthorizationstatus)*