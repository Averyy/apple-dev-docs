# LanguageModelExecutorGenerationChannel.ReasoningSignature

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Payload for a reasoning entry’s signature update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ReasoningSignature
```

#### Overview

The signature is an opaque, producer-supplied token; each `updateSignature` event replaces the prior value wholesale. `tokenCount` is the producer’s count of tokens carried by the signature, used for usage accounting.

## Topics

### Handling the reasoning signature
- [var signature: Data](./reasoningsignature/signature.md)
  The opaque token that authenticates the reasoning entry.
- [var tokenCount: Int](./reasoningsignature/tokencount.md)
  The number of the tokens the signature carries.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoningsignature)*