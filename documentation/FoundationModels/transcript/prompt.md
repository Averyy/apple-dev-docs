# Transcript.Prompt

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A prompt from the user to the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct Prompt
```

## Overview

Prompts typically contain content sourced directly from the user, though you may choose to augment prompts by interpolating content from end users into a template that you control.

## Topics

### Creating a prompt
- [init(id: String, segments: [Transcript.Segment], options: GenerationOptions, responseFormat: Transcript.ResponseFormat?)](./prompt/init%28id,segments,options,responseformat%29.md)
  Creates a prompt.
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment], options: GenerationOptions, responseFormat: Transcript.ResponseFormat?, contextOptions: ContextOptions)](./prompt/init%28id,metadata,segments,options,responseformat,contextoptions%29.md)
  Creates a prompt.
### Inspecting a prompt
- [var id: String](./prompt/id.md)
  The identifier of the prompt.
- [var responseFormat: Transcript.ResponseFormat?](./prompt/responseformat.md)
  An optional response format that describes the desired output structure.
- [var segments: [Transcript.Segment]](./prompt/segments.md)
  Ordered prompt segments.
- [var options: GenerationOptions](./prompt/options.md)
  Generation options associated with the prompt.
- [var contextOptions: ContextOptions](./prompt/contextoptions.md)
  Configuration of the prompt.
- [var metadata: [String : GeneratedContent]](./prompt/metadata.md)
  Metadata provided as part of this prompt.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transcript entries
- [Transcript.Entry](./entry.md)
  An entry in a transcript.
- [Transcript.Instructions](./instructions.md)
  Instructions you provide to the model that define its behavior.
- [Transcript.Response](./response.md)
  A response from the model.
- [Transcript.Reasoning](./reasoning.md)
  A reasoning entry from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/prompt)*