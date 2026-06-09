# LanguageModelExecutorGenerationChannel.Usage

**Framework**: Foundation Models  
**Kind**: struct

Snapshot of an entry’s token totals.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Usage
```

#### Overview

Producers report the current cumulative totals on every update and consumers replace prior totals wholesale.

## Topics

### Creating a usage token instance
- [init(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output)](languagemodelexecutorgenerationchannel/usage/init(input:output:).md)
  Creates a usage update.
### Updating the token counts
- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](languagemodelexecutorgenerationchannel/usage/input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelExecutorGenerationChannel.Usage.Input](languagemodelexecutorgenerationchannel/usage/input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](languagemodelexecutorgenerationchannel/usage/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelExecutorGenerationChannel.Usage.Output](languagemodelexecutorgenerationchannel/usage/output-swift.struct.md)
  Token counts for the output produced by the model.

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
- [LanguageModelExecutorGenerationChannel.TextFragment](languagemodelexecutorgenerationchannel/textfragment.md)
  Append text to a streaming entry’s current text segment. Used by both [`LanguageModelExecutorGenerationChannel.Response.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:).md) and [`LanguageModelExecutorGenerationChannel.Reasoning.Action.appendText(_:)`](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/appendtext(_:).md).
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  Replace a streaming entry’s current text segment with `content`.
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage)*