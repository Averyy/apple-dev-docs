# UINotificationFeedbackGenerator

**Framework**: UIKit  
**Kind**: class

A concrete feedback generator subclass that creates haptics to communicate successes, failures, and warnings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UINotificationFeedbackGenerator
```

#### Overview

Use notification feedback to communicate that a task or action succeeded, failed, or produced a warning of some kind.

For more information, read [`Playing haptic feedback in your app`](https://developer.apple.com/documentation/ApplePencil/playing-haptic-feedback-in-your-app).

## Topics

### Producing notification feedback
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType)](uinotificationfeedbackgenerator/notificationoccurred(_:).md)
  Triggers notification feedback.
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType, at: CGPoint)](uinotificationfeedbackgenerator/notificationoccurred(_:at:).md)
  Triggers notification feedback at the specified location.
- [UINotificationFeedbackGenerator.FeedbackType](uinotificationfeedbackgenerator/feedbacktype.md)
  The type of notification that a notification feedback generator object generates.

## Relationships

### Inherits From
- [UIFeedbackGenerator](uifeedbackgenerator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Playing haptic feedback in your app](../ApplePencil/playing-haptic-feedback-in-your-app.md)
  Provide tactile feedback when people perform certain actions in your app.
- [class UIFeedbackGenerator](uifeedbackgenerator.md)
  The abstract superclass for all feedback generators.
- [class UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to simulate physical impacts.
- [class UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate a change in selection.
- [class UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md)
  A concrete feedback generator subclass that creates haptics to indicate events on a drawing canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator)*