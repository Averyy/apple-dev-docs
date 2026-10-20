# UINotificationFeedbackGenerator.FeedbackType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of notification that a notification feedback generator object generates.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum FeedbackType
```

```c
enum UINotificationFeedbackType : NSInteger;
```

## Topics

### Constants
- [UINotificationFeedbackGenerator.FeedbackType.error](./feedbacktype/error.md)
  A notification feedback type that indicates a task has failed.
- [UINotificationFeedbackGenerator.FeedbackType.success](./feedbacktype/success.md)
  A notification feedback type that indicates a task has completed successfully.
- [UINotificationFeedbackGenerator.FeedbackType.warning](./feedbacktype/warning.md)
  A notification feedback type that indicates a task has produced a warning.
### Initializers
- [init?(rawValue: Int)](./feedbacktype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Producing notification feedback
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType)](./notificationoccurred%28_%29.md)
  Triggers notification feedback.
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType, at: CGPoint)](./notificationoccurred%28_,at%29.md)
  Triggers notification feedback at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator/feedbacktype)*