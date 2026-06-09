# feedback(title:shortTitle:status:_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that handles user feedback (positive, neutral, or negative) for the current content.

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
static func feedback(title: String? = nil, shortTitle: String? = nil, status: MediaCommand.FeedbackStatus = .neutral, _ action: @escaping (MediaCommand.FeedbackStatus) async throws -> Void) -> MediaCommand
```

## Parameters

- `title`: A localized string that describes the context of the command.
- `shortTitle`: A shortened version of the title.
- `status`: The current feedback status for the content.
- `action`: The closure the system calls when the user changes the feedback status.

## See Also

- [MediaCommand.FeedbackStatus](mediacommand/feedbackstatus.md)
  The feedback status for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/feedback(title:shorttitle:status:_:))*