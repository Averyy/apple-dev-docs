# LanguageModelExecutorGenerationChannel.Event

**Framework**: Foundation Models  
**Kind**: protocol

A typed event that can be sent on a generation channel.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol Event : Sendable
```

## Topics

### Handling the channel events
- [static func response(entryID: String?, action: LanguageModelExecutorGenerationChannel.Response.Action) -> Self](languagemodelexecutorgenerationchannel/event/response(entryid:action:).md)
  Constructs a [`LanguageModelExecutorGenerationChannel.Response`](languagemodelexecutorgenerationchannel/response.md) event for use at `channel.send(.response(entryID:action:))` call sites.
- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> Self](languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:).md)
  Constructs a [`LanguageModelExecutorGenerationChannel.ToolCalls`](languagemodelexecutorgenerationchannel/toolcalls.md) event for use at `channel.send(.toolCalls(entryID:action:))` call sites.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> Self](languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:).md)
  Constructs a [`LanguageModelExecutorGenerationChannel.Reasoning`](languagemodelexecutorgenerationchannel/reasoning.md) event for use at `channel.send(.reasoning(entryID:action:))` call sites.
### Configuring the channel
- [var kind: LanguageModelExecutorGenerationChannel.EventKind](languagemodelexecutorgenerationchannel/event/kind.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [LanguageModelExecutorGenerationChannel.Reasoning](languagemodelexecutorgenerationchannel/reasoning.md)
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)

## See Also

- [func send(some LanguageModelExecutorGenerationChannel.Event) async](languagemodelexecutorgenerationchannel/send(_:).md)
  Performs a send on the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event)*