# response(entryID:action:)

**Framework**: Foundation Models  
**Kind**: method

Constructs a [`LanguageModelExecutorGenerationChannel.Response`](languagemodelexecutorgenerationchannel/response.md) event for use at `channel.send(.response(entryID:action:))` call sites.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func response(entryID: String? = nil, action: LanguageModelExecutorGenerationChannel.Response.Action) -> Self
```

## See Also

- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> Self](languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:).md)
  Constructs a [`LanguageModelExecutorGenerationChannel.ToolCalls`](languagemodelexecutorgenerationchannel/toolcalls.md) event for use at `channel.send(.toolCalls(entryID:action:))` call sites.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> Self](languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:).md)
  Constructs a [`LanguageModelExecutorGenerationChannel.Reasoning`](languagemodelexecutorgenerationchannel/reasoning.md) event for use at `channel.send(.reasoning(entryID:action:))` call sites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event/response(entryid:action:))*