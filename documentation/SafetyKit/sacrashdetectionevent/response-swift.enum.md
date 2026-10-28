# SACrashDetectionEvent.Response

**Framework**: SafetyKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum SACrashDetectionEventResponse : NSInteger;
```

## Overview

The Crash Detection event response indicates whether the system attempted to dial the Emergency SOS - Call After Severe Crash provider, depending on the setting in the Settings app.

## Topics

### Determining responses
- [SACrashDetectionEvent.Response.attempted](./response-swift.enum/attempted.md)
  The system attempted to dial the Emergency SOS - Call After Severe Crash provider.
- [SACrashDetectionEvent.Response.disabled](./response-swift.enum/disabled.md)
  The system couldn’t contact the Emergency SOS - Call After Severe Crash provider because the feature is off in the Settings app.
### Initializers
- [init?(rawValue: Int)](./response-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to a crash
- [class SAEmergencyResponseManager](../saemergencyresponsemanager.md)
  Provides actions in response to a Crash Detection event.
- [protocol SAEmergencyResponseDelegate](../saemergencyresponsedelegate.md)
  The interface for receiving updates about a requested emergency response action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/response-swift.enum)*