# LanguageModelExecutorGenerationChannel.ToolCalls

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ToolCalls
```

## Overview

Events for a specific tool call route through [`toolCall(id:name:action:)`](./toolcalls/action-swift.struct/toolcall%28id,name,action%29.md). Use [`removeToolCall(id:)`](./toolcalls/action-swift.struct/removetoolcall%28id%29.md) to drop a tool call the model retracted.

## Topics

### Handling tool calls
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](./toolcalls/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action](./toolcalls/action-swift.struct.md)
  An operation that can be performed on a tool-calls entry.
- [var entryID: String?](./toolcalls/entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall](./toolcalls/toolcall.md)
  A per-tool-call event payload.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the event types
- [LanguageModelExecutorGenerationChannel.Metadata](./metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.Reasoning](./reasoning.md)
  A reasoning event.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](./reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextFragment](./textfragment.md)
  Text appended to a streaming entry’s current text segment.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](./textsegmentreplacement.md)
  A replacement for a streaming entry’s current text segment.
- [LanguageModelExecutorGenerationChannel.Response](./response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.Usage](./usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls)*