# reasoning(entryID:action:)

**Framework**: Foundation Models  
**Kind**: method

A reasoning event addressed to a transcript entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func reasoning(entryID: String? = nil, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> LanguageModelExecutorGenerationChannel.Event
```

## Parameters

- `entryID`: The reasoning entry this event targets. Pass `nil` to coalesce consecutive reasoning deltas into the trailing reasoning entry; pass an explicit id when you need a stable anchor.
- `action`: The operation to perform on the reasoning entry.

## See Also

- [static func response(entryID: String?, action: LanguageModelExecutorGenerationChannel.Response.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/response(entryid:action:).md)
  A response event addressed to a transcript entry.
- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:).md)
  A tool-calls event addressed to a transcript entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:))*