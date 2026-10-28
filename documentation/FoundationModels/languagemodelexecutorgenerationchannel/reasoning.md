# LanguageModelExecutorGenerationChannel.Reasoning

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A reasoning event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Reasoning
```

## Overview

A per-entry reasoning text, segment replacements, signature updates, metadata, or usage. Reasoning events are peers of [`LanguageModelExecutorGenerationChannel.Response`](./response.md) and [`LanguageModelExecutorGenerationChannel.ToolCalls`](./toolcalls.md).

## Topics

### Handling reasoning
- [var action: LanguageModelExecutorGenerationChannel.Reasoning.Action](./reasoning/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.Reasoning.Action](./reasoning/action-swift.struct.md)
  An operation that can be performed on a reasoning entry.
- [var entryID: String?](./reasoning/entryid.md)
  The identifier for the entry.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the event types
- [LanguageModelExecutorGenerationChannel.Metadata](./metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](./reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextFragment](./textfragment.md)
  Text appended to a streaming entry’s current text segment.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](./textsegmentreplacement.md)
  A replacement for a streaming entry’s current text segment.
- [LanguageModelExecutorGenerationChannel.Response](./response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](./toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](./usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning)*