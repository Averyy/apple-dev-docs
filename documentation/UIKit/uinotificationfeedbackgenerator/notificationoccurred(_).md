# notificationOccurred(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers notification feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func notificationOccurred(_ notificationType: UINotificationFeedbackGenerator.FeedbackType)
```

```objc
- (void) notificationOccurred:(UINotificationFeedbackType) notificationType;
```

#### Discussion

This method tells the generator that a task or action has succeeded, failed, or produced a warning. In response, the generator may play the appropriate haptics, based on the provided [`UINotificationFeedbackGenerator.FeedbackType`](./feedbacktype.md) value.

For more information on setting up a feedback generator, see the [`UIFeedbackGenerator`](../uifeedbackgenerator.md) class.

## Parameters

- `notificationType`: The type of notification feedback. For a list of valid notification types, see the [`UINotificationFeedbackGenerator.FeedbackType`](./feedbacktype.md) enumeration.

## See Also

### Related Documentation
- [func prepare()](../uifeedbackgenerator/prepare%28%29.md)
  Prepares the generator to trigger feedback.
### Producing notification feedback
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType, at: CGPoint)](./notificationoccurred%28_,at%29.md)
  Triggers notification feedback at the specified location.
- [UINotificationFeedbackGenerator.FeedbackType](./feedbacktype.md)
  The type of notification that a notification feedback generator object generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred(_:))*