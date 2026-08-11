# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall

**Framework**: Foundation Models  
**Kind**: struct

A per-tool-call event payload.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ToolCall
```

#### Overview

The `id` and `name` route the event to a specific tool call within the `ToolCalls` entry. The`action` names the mutation.

## Topics

### Handling a tool call
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct.md)
  An operation that can be performed on a tool call.
- [var id: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/id.md)
  The identifier for the tool call.
- [var name: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/name.md)
  The name of the tool call.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment](languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment.md)
  Argument text appended to this tool call.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct.md)
  An operation that can be performed on a tool-calls entry.
- [var entryID: String?](languagemodelexecutorgenerationchannel/toolcalls/entryid.md)
  The identifier for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall)*