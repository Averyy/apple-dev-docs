# MediaCommand.FeedbackStatus

**Framework**: Now Playing  
**Kind**: enum

The feedback status for a media item.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum FeedbackStatus
```

#### Overview

Use this to represent whether the user has expressed positive, negative, or no preference for the current content.

## Topics

### Enumeration Cases
- [MediaCommand.FeedbackStatus.negative](mediacommand/feedbackstatus/negative.md)
  The user has expressed negative feedback for the content.
- [MediaCommand.FeedbackStatus.neutral](mediacommand/feedbackstatus/neutral.md)
  The user has not expressed a preference.
- [MediaCommand.FeedbackStatus.positive](mediacommand/feedbackstatus/positive.md)
  The user has expressed positive feedback for the content.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func feedback(title: String?, shortTitle: String?, status: MediaCommand.FeedbackStatus, (MediaCommand.FeedbackStatus) async throws -> Void) -> MediaCommand](mediacommand/feedback(title:shorttitle:status:_:).md)
  Creates a command that handles user feedback (positive, neutral, or negative) for the current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/feedbackstatus)*