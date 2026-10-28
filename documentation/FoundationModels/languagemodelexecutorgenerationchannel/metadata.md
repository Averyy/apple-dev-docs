# LanguageModelExecutorGenerationChannel.Metadata

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Snapshot of an entry’s metadata dictionary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Metadata
```

## Overview

Each event replaces the prior metadata wholesale; keys absent from `values` are considered removed.

## Topics

### Handling the metadata values
- [var values: [String : GeneratedContent]](./metadata/values.md)
  The metadata key-value pairs for the entry.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the event types
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
- [LanguageModelExecutorGenerationChannel.ToolCalls](./toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](./usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/metadata)*