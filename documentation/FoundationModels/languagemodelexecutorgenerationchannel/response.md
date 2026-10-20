# LanguageModelExecutorGenerationChannel.Response

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Response
```

## Topics

### Handling a response
- [var action: LanguageModelExecutorGenerationChannel.Response.Action](./response/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.Response.Action](./response/action-swift.struct.md)
  An operation that can be performed on a response entry.
- [var entryID: String?](./response/entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](./textsegmentreplacement.md)
  A replacement for a streaming entry’s current text segment.

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
- [LanguageModelExecutorGenerationChannel.ToolCalls](./toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](./usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response)*