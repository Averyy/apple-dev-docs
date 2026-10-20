# notificationOccurred(_:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers notification feedback at the specified location.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+

## Declaration

```swift
func notificationOccurred(_ notificationType: UINotificationFeedbackGenerator.FeedbackType, at location: CGPoint)
```

```objc
- (void) notificationOccurred:(UINotificationFeedbackType) notificationType atLocation:(CGPoint) location;
```

## See Also

### Producing notification feedback
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType)](./notificationoccurred%28_%29.md)
  Triggers notification feedback.
- [UINotificationFeedbackGenerator.FeedbackType](./feedbacktype.md)
  The type of notification that a notification feedback generator object generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/notificationoccurred(_:at:))*