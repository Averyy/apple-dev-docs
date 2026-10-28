# MediaCommand.FeedbackStatus

**Framework**: Now Playing  
**Kind**: enum  
**Role**: Enumeration

The feedback status for a media item.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum FeedbackStatus
```

## Overview

Use this to represent whether the user has expressed positive, negative, or no preference for the current content.

## Topics

### Enumeration Cases
- [MediaCommand.FeedbackStatus.negative](./feedbackstatus/negative.md)
  The user has expressed negative feedback for the content.
- [MediaCommand.FeedbackStatus.neutral](./feedbackstatus/neutral.md)
  The user has not expressed a preference.
- [MediaCommand.FeedbackStatus.positive](./feedbackstatus/positive.md)
  The user has expressed positive feedback for the content.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing feedback
- [static func feedback(title: String?, shortTitle: String?, status: MediaCommand.FeedbackStatus, (MediaCommand.FeedbackStatus) async throws -> Void) -> MediaCommand](./feedback%28title,shorttitle,status,_%29.md)
  Creates a command that handles user feedback (positive, neutral, or negative) for the current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/feedbackstatus)*