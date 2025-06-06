# NSHapticFeedbackManager.PerformanceTime

**Framework**: AppKit  
**Kind**: enum

A time at which to provide haptic feedback to the user.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum PerformanceTime
```

## Topics

### Constants
- [NSHapticFeedbackManager.PerformanceTime.default](nshapticfeedbackmanager/performancetime/default.md)
  Allows the system to choose the most appropriate time for feedback to be provided. Currently, this is the next time the screen is updated.
- [NSHapticFeedbackManager.PerformanceTime.now](nshapticfeedbackmanager/performancetime/now.md)
  Instructs the system to provide immediate haptic feedback to the user, rather than waiting for synchronization to occur with something visual occurring on screen.
- [NSHapticFeedbackManager.PerformanceTime.drawCompleted](nshapticfeedbackmanager/performancetime/drawcompleted.md)
  Instructs the system to provide haptic feedback to the user the next time the screen is updated.
### Initializers
- [init?(rawValue: UInt)](nshapticfeedbackmanager/performancetime/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSHapticFeedbackManager.FeedbackPattern](nshapticfeedbackmanager/feedbackpattern.md)
  A pattern of haptic feedback to be provided to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/performancetime)*