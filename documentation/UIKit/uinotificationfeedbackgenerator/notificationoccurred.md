# notificationOccurred(_:)

**Framework**: UIKit  
**Kind**: method

Triggers notification feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func notificationOccurred(_ notificationType: UINotificationFeedbackGenerator.FeedbackType)
```

#### Discussion

This method tells the generator that a task or action has succeeded, failed, or produced a warning. In response, the generator may play the appropriate haptics, based on the provided [`UINotificationFeedbackGenerator.FeedbackType`](uinotificationfeedbackgenerator/feedbacktype.md) value.

For more information on setting up a feedback generator, see the [`UIFeedbackGenerator`](uifeedbackgenerator.md) class.

## Parameters

- `notificationType`: The type of notification feedback. For a list of valid notification types, see the   enumeration.

## See Also

- [func prepare()](uifeedbackgenerator/prepare.md)
  Prepares the generator to trigger feedback.
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType, at: CGPoint)](uinotificationfeedbackgenerator/notificationoccurred(_:at:).md)
  Triggers notification feedback at the specified location.
- [UINotificationFeedbackGenerator.FeedbackType](uinotificationfeedbackgenerator/feedbacktype.md)
  The type of notification that a notification feedback generator object generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred(_:))*