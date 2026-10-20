# LanguageModelExecutorGenerationChannel.Event

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A generation event sent on a generation channel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Event
```

#### Overview

Construct one with a leading-dot factory — [`response(entryID:action:)`](./event/response%28entryid,action%29.md), [`reasoning(entryID:action:)`](./event/reasoning%28entryid,action%29.md), or [`toolCalls(entryID:action:)`](./event/toolcalls%28entryid,action%29.md) — and pass it to [`send(_:)`](./send%28_%29.md).

## Topics

### Handling the channel events
- [static func response(entryID: String?, action: LanguageModelExecutorGenerationChannel.Response.Action) -> LanguageModelExecutorGenerationChannel.Event](./event/response%28entryid,action%29.md)
  A response event addressed to a transcript entry.
- [static func toolCalls(entryID: String?, action: LanguageModelExecutorGenerationChannel.ToolCalls.Action) -> LanguageModelExecutorGenerationChannel.Event](./event/toolcalls%28entryid,action%29.md)
  A tool-calls event addressed to a transcript entry.
- [static func reasoning(entryID: String?, action: LanguageModelExecutorGenerationChannel.Reasoning.Action) -> LanguageModelExecutorGenerationChannel.Event](./event/reasoning%28entryid,action%29.md)
  A reasoning event addressed to a transcript entry.
### Type Methods
- [static func data(entryID: String?, action: LanguageModelExecutorGenerationChannel.DataEntry.Action) -> LanguageModelExecutorGenerationChannel.Event](./event/data%28entryid,action%29.md)
  A data-entry event addressed to a transcript entry.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending an event
- [func send(LanguageModelExecutorGenerationChannel.Event) async](./send%28_%29.md)
  Sends a generation event on the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/event)*