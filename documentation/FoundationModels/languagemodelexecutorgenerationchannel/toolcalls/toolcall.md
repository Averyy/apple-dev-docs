# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A per-tool-call event payload.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ToolCall
```

## Overview

The `id` and `name` route the event to a specific tool call within the `ToolCalls` entry. The`action` names the mutation.

## Topics

### Handling a tool call
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./toolcall/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./toolcall/action-swift.struct.md)
  An operation that can be performed on a tool call.
- [var id: String](./toolcall/id.md)
  The identifier for the tool call.
- [var name: String](./toolcall/name.md)
  The name of the tool call.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment](./toolcall/argumentsfragment.md)
  Argument text appended to this tool call.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Handling tool calls
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.struct.md)
  An operation that can be performed on a tool-calls entry.
- [var entryID: String?](./entryid.md)
  The identifier for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall)*