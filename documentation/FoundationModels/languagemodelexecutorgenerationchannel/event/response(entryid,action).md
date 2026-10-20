# response(entryID:action:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

A response event addressed to a transcript entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func response(entryID: String? = nil, action: LanguageModelExecutorGenerationChannel.Response.Action) -> LanguageModelExecutorGenerationChannel.Event
```

## Parameters

- `entryID`: The response entry this event targets. Pass `nil` to let the framework coalesce consecutive response events into a single entry; pass an explicit id to anchor the event to a specific entry.
- `action`: The operation to perform on the response entry.

## See Also

### Handling the channel events
- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> LanguageModelExecutorGenerationChannel.Event](./toolcalls%28entryid,action%29.md)
  A tool-calls event addressed to a transcript entry.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> LanguageModelExecutorGenerationChannel.Event](./reasoning%28entryid,action%29.md)
  A reasoning event addressed to a transcript entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event/response(entryid:action:))*