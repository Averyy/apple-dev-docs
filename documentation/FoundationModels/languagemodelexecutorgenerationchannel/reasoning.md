# LanguageModelExecutorGenerationChannel.Reasoning

**Framework**: Foundation Models  
**Kind**: struct

A reasoning event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Reasoning
```

#### Overview

A per-entry reasoning text, segment replacements, signature updates, metadata, or usage. Reasoning events are peers of [`LanguageModelExecutorGenerationChannel.Response`](languagemodelexecutorgenerationchannel/response.md) and [`LanguageModelExecutorGenerationChannel.ToolCalls`](languagemodelexecutorgenerationchannel/toolcalls.md).

## Topics

### Handling reasoning
- [var action: LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum.md)
- [var entryID: String?](languagemodelexecutorgenerationchannel/reasoning/entryid.md)
  The identifier for the entry.

## Relationships

### Conforms To
- [LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelExecutorGenerationChannel.EventKind](languagemodelexecutorgenerationchannel/eventkind.md)
  A kind of event that can be sent on a generation channel.
- [LanguageModelExecutorGenerationChannel.Metadata](languagemodelexecutorgenerationchannel/metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](languagemodelexecutorgenerationchannel/reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextFragment](languagemodelexecutorgenerationchannel/textfragment.md)
  Append text to a streaming entry’s current text segment. Used by both [`LanguageModelExecutorGenerationChannel.Response.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:).md) and [`LanguageModelExecutorGenerationChannel.Reasoning.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/appendtext(_:).md).
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  Replace a streaming entry’s current text segment with `content`.
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](languagemodelexecutorgenerationchannel/usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning)*