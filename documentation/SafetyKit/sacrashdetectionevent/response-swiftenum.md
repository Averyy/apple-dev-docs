# SACrashDetectionEvent.Response

**Framework**: SafetyKit  
**Kind**: enum

An enumeration that defines possible emergency responses to a Crash Detection event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
enum Response
```

#### Overview

The Crash Detection event response indicates whether the system attempted to dial the Emergency SOS - Call After Severe Crash provider, depending on the setting in the Settings app.

## Topics

### Determining responses
- [SACrashDetectionEvent.Response.attempted](sacrashdetectionevent/response-swift.enum/attempted.md)
  The system attempted to dial the Emergency SOS - Call After Severe Crash provider.
- [SACrashDetectionEvent.Response.disabled](sacrashdetectionevent/response-swift.enum/disabled.md)
  The system couldn’t contact the Emergency SOS - Call After Severe Crash provider because the feature is off in the Settings app.
### Initializers
- [init?(rawValue: Int)](sacrashdetectionevent/response-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class SAEmergencyResponseManager](saemergencyresponsemanager.md)
  Provides actions in response to a Crash Detection event.
- [protocol SAEmergencyResponseDelegate](saemergencyresponsedelegate.md)
  The interface for receiving updates about a requested emergency response action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/response-swift.enum)*