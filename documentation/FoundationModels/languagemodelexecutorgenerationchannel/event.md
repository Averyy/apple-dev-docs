# LanguageModelExecutorGenerationChannel.Event

**Framework**: Foundation Models  
**Kind**: struct

A generation event sent on a generation channel.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Event
```

#### Overview

Construct one with a leading-dot factory — [`response(entryID:action:)`](languagemodelexecutorgenerationchannel/event/response(entryid:action:).md), [`reasoning(entryID:action:)`](languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:).md), or [`toolCalls(entryID:action:)`](languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:).md) — and pass it to [`send(_:)`](languagemodelexecutorgenerationchannel/send(_:).md).

## Topics

### Handling the channel events
- [static func response(entryID: String?, action: LanguageModelExecutorGenerationChannel.Response.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/response(entryid:action:).md)
  A response event addressed to a transcript entry.
- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/toolcalls(entryid:action:).md)
  A tool-calls event addressed to a transcript entry.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event/reasoning(entryid:action:).md)
  A reasoning event addressed to a transcript entry.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func send(LanguageModelExecutorGenerationChannel.Event) async](languagemodelexecutorgenerationchannel/send(_:).md)
  Sends a generation event on the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event)*