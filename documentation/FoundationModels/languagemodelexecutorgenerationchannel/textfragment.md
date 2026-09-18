# LanguageModelExecutorGenerationChannel.TextFragment

**Framework**: Foundation Models  
**Kind**: struct

Text appended to a streaming entry’s current text segment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct TextFragment
```

#### Overview

Use this type when appending text with [`LanguageModelExecutorGenerationChannel.Response`](languagemodelexecutorgenerationchannel/response.md) and [`LanguageModelExecutorGenerationChannel.Reasoning`](languagemodelexecutorgenerationchannel/reasoning.md) actions.

## Topics

### Handling the text fragment
- [var content: String](languagemodelexecutorgenerationchannel/textfragment/content.md)
  The text to append to the entry’s current text segment.
- [var tokenCount: Int](languagemodelexecutorgenerationchannel/textfragment/tokencount.md)
  The number of tokens the text carries.
- [var segmentID: String?](languagemodelexecutorgenerationchannel/textfragment/segmentid.md)
  The identifier of the text segment to append to, or empty to append to the current segment.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [LanguageModelExecutorGenerationChannel.Metadata](languagemodelexecutorgenerationchannel/metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.Reasoning](languagemodelexecutorgenerationchannel/reasoning.md)
  A reasoning event.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](languagemodelexecutorgenerationchannel/reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  A replacement for a streaming entry’s current text segment.
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](languagemodelexecutorgenerationchannel/usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/textfragment)*