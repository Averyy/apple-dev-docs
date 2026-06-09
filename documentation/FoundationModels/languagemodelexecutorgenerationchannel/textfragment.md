# LanguageModelExecutorGenerationChannel.TextFragment

**Framework**: Foundation Models  
**Kind**: struct

Append text to a streaming entry’s current text segment. Used by both [`LanguageModelExecutorGenerationChannel.Response.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:).md) and [`LanguageModelExecutorGenerationChannel.Reasoning.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/appendtext(_:).md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct TextFragment
```

## Topics

### Handling the text fragment
- [var content: String](languagemodelexecutorgenerationchannel/textfragment/content.md)
- [var tokenCount: Int](languagemodelexecutorgenerationchannel/textfragment/tokencount.md)
- [var segmentID: String?](languagemodelexecutorgenerationchannel/textfragment/segmentid.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelExecutorGenerationChannel.EventKind](languagemodelexecutorgenerationchannel/eventkind.md)
  A kind of event that can be sent on a generation channel.
- [LanguageModelExecutorGenerationChannel.Metadata](languagemodelexecutorgenerationchannel/metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.Reasoning](languagemodelexecutorgenerationchannel/reasoning.md)
  A reasoning event.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](languagemodelexecutorgenerationchannel/reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  Replace a streaming entry’s current text segment with `content`.
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](languagemodelexecutorgenerationchannel/usage.md)
  Snapshot of an entry’s token totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/textfragment)*