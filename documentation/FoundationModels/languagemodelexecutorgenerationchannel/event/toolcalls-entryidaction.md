# toolCalls(entryID:action:)

**Framework**: Foundation Models  
**Kind**: method

A tool-calls event addressed to a transcript entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func toolCalls(entryID: String? = nil, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> LanguageModelExecutorGenerationChannel.Event
```

## Parameters

- `entryID`: The tool-calls entry this event targets. Pass `nil` to let the framework coalesce consecutive tool-calls events into a single entry; pass an explicit id to anchor the event to a specific entry.
- `action`: The operation to perform on the tool-calls entry.

## See Also

- [static func response(entryID: String?, action: LanguageModelExecutorGenerationChannel.Response.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/response(entryid:action:).md)
  A response event addressed to a transcript entry.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:).md)
  A reasoning event addressed to a transcript entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:))*