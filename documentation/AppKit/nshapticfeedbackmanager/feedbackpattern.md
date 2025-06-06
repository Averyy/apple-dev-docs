# NSHapticFeedbackManager.FeedbackPattern

**Framework**: AppKit  
**Kind**: enum

A pattern of haptic feedback to be provided to the user.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum FeedbackPattern
```

## Topics

### Constants
- [NSHapticFeedbackManager.FeedbackPattern.generic](nshapticfeedbackmanager/feedbackpattern/generic.md)
  A general haptic feedback pattern. Use this when no other feedback patterns apply.
- [NSHapticFeedbackManager.FeedbackPattern.alignment](nshapticfeedbackmanager/feedbackpattern/alignment.md)
  A haptic feedback pattern to be used in response to the alignment of an object the user is dragging around. For example, this pattern of feedback could be used in a drawing app when the user drags a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/minimum or end/maximum of something, such as a track view in an audio/video app.
- [NSHapticFeedbackManager.FeedbackPattern.levelChange](nshapticfeedbackmanager/feedbackpattern/levelchange.md)
  A haptic feedback pattern to be used as the user moves between discrete levels of pressure. This pattern of feedback is used by multilevel accelerator buttons (class [`NSMultiLevelAcceleratorButton`](nsmultilevelacceleratorbutton.md)).
### Initializers
- [init?(rawValue: Int)](nshapticfeedbackmanager/feedbackpattern/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSHapticFeedbackManager.PerformanceTime](nshapticfeedbackmanager/performancetime.md)
  A time at which to provide haptic feedback to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/feedbackpattern)*