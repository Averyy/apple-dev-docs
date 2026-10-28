# CMFallDetectionEvent.UserResolution

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

User resolutions for fall detection events.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
enum UserResolution
```

```c
enum CMFallDetectionEventUserResolution : NSInteger;
```

## Overview

The resolution of an event reflects the user’s action in response to the fall detection notification. For example, the user might tap a button to respond inside the notification, or press the digital crown to dismiss the notification.

## Topics

### Resolutions
- [CMFallDetectionEvent.UserResolution.confirmed](./userresolution/confirmed.md)
  The user confirmed the event.
- [CMFallDetectionEvent.UserResolution.dismissed](./userresolution/dismissed.md)
  The user dismissed the fall event alert, but didn’t explicitly confirm or reject the event.
- [CMFallDetectionEvent.UserResolution.rejected](./userresolution/rejected.md)
  The user rejected the fall event.
- [CMFallDetectionEvent.UserResolution.unresponsive](./userresolution/unresponsive.md)
  The user didn’t respond to the fall event and the system hasn’t detected recovery motions.
### Initializers
- [init?(rawValue: Int)](./userresolution/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Fall Data
- [var resolution: CMFallDetectionEvent.UserResolution](./resolution.md)
  The event’s resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution)*