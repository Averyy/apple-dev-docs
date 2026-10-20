# NSHapticFeedbackManager.PerformanceTime

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A time at which to provide haptic feedback to the user.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum PerformanceTime
```

```c
enum NSHapticFeedbackPerformanceTime : NSUInteger;
```

## Topics

### Constants
- [NSHapticFeedbackManager.PerformanceTime.default](./performancetime/default.md)
  Allows the system to choose the most appropriate time for feedback to be provided. Currently, this is the next time the screen is updated.
- [NSHapticFeedbackManager.PerformanceTime.now](./performancetime/now.md)
  Instructs the system to provide immediate haptic feedback to the user, rather than waiting for synchronization to occur with something visual occurring on screen.
- [NSHapticFeedbackManager.PerformanceTime.drawCompleted](./performancetime/drawcompleted.md)
  Instructs the system to provide haptic feedback to the user the next time the screen is updated.
### Initializers
- [init?(rawValue: UInt)](./performancetime/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [NSHapticFeedbackManager.FeedbackPattern](./feedbackpattern.md)
  A pattern of haptic feedback to be provided to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/performancetime)*