# UINotificationFeedbackGenerator.FeedbackType

**Framework**: UIKit  
**Kind**: enum

The type of notification that a notification feedback generator object generates.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum FeedbackType
```

## Topics

### Constants
- [UINotificationFeedbackGenerator.FeedbackType.error](uinotificationfeedbackgenerator/feedbacktype/error.md)
  A notification feedback type that indicates a task has failed.
- [UINotificationFeedbackGenerator.FeedbackType.success](uinotificationfeedbackgenerator/feedbacktype/success.md)
  A notification feedback type that indicates a task has completed successfully.
- [UINotificationFeedbackGenerator.FeedbackType.warning](uinotificationfeedbackgenerator/feedbacktype/warning.md)
  A notification feedback type that indicates a task has produced a warning.
### Initializers
- [init?(rawValue: Int)](uinotificationfeedbackgenerator/feedbacktype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType)](uinotificationfeedbackgenerator/notificationoccurred(_:).md)
  Triggers notification feedback.
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType, at: CGPoint)](uinotificationfeedbackgenerator/notificationoccurred(_:at:).md)
  Triggers notification feedback at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype)*