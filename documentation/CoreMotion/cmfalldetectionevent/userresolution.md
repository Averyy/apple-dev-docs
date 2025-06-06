# CMFallDetectionEvent.UserResolution

**Framework**: Core Motion  
**Kind**: enum

User resolutions for fall detection events.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
enum UserResolution
```

#### Overview

The resolution of an event reflects the user’s action in response to the fall detection notification. For example, the user might tap a button to respond inside the notification, or press the digital crown to dismiss the notification.

## Topics

### Resolutions
- [CMFallDetectionEvent.UserResolution.confirmed](cmfalldetectionevent/userresolution/confirmed.md)
  The user confirmed the event.
- [CMFallDetectionEvent.UserResolution.dismissed](cmfalldetectionevent/userresolution/dismissed.md)
  The user dismissed the fall event alert, but didn’t explicitly confirm or reject the event.
- [CMFallDetectionEvent.UserResolution.rejected](cmfalldetectionevent/userresolution/rejected.md)
  The user rejected the fall event.
- [CMFallDetectionEvent.UserResolution.unresponsive](cmfalldetectionevent/userresolution/unresponsive.md)
  The user didn’t respond to the fall event and the system hasn’t detected recovery motions.
### Initializers
- [init?(rawValue: Int)](cmfalldetectionevent/userresolution/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var resolution: CMFallDetectionEvent.UserResolution](cmfalldetectionevent/resolution.md)
  The event’s resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent/userresolution)*