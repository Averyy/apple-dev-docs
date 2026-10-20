# LanguageModelExecutorGenerationChannel.Usage

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Snapshot of an entry’s token totals.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Usage
```

#### Overview

Producers report the current cumulative totals on every update, and consumers replace prior totals wholesale.

## Topics

### Creating a usage token instance
- [init(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent])](./usage/init%28input,output,metadata%29.md)
  Creates a usage update.
### Updating the token counts
- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](./usage/input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelExecutorGenerationChannel.Usage.Input](./usage/input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](./usage/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelExecutorGenerationChannel.Usage.Output](./usage/output-swift.struct.md)
  Token counts for the output produced by the model.
### Accessing the metadata
- [var metadata: [String : GeneratedContent]](./usage/metadata.md)
  The additional metadata with a token count.

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
- [LanguageModelExecutorGenerationChannel.ToolCalls](./toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage)*