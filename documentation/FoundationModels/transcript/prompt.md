# Transcript.Prompt

**Framework**: Foundation Models  
**Kind**: struct

A prompt from the user to the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Prompt
```

#### Overview

Prompts typically contain content sourced directly from the user, though you may choose to augment prompts by interpolating content from end users into a template that you control.

## Topics

### Creating a prompt
- [init(id: String, segments: [Transcript.Segment], options: GenerationOptions, responseFormat: Transcript.ResponseFormat?)](transcript/prompt/init(id:segments:options:responseformat:).md)
  Creates a prompt.
- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment], options: GenerationOptions, responseFormat: Transcript.ResponseFormat?, contextOptions: ContextOptions)](transcript/prompt/init(id:metadata:segments:options:responseformat:contextoptions:).md)
  Creates a prompt.
### Inspecting a prompt
- [var id: String](transcript/prompt/id.md)
  The identifier of the prompt.
- [var responseFormat: Transcript.ResponseFormat?](transcript/prompt/responseformat.md)
  An optional response format that describes the desired output structure.
- [var segments: [Transcript.Segment]](transcript/prompt/segments.md)
  Ordered prompt segments.
- [var options: GenerationOptions](transcript/prompt/options.md)
  Generation options associated with the prompt.
- [var contextOptions: ContextOptions](transcript/prompt/contextoptions.md)
  Configuration of the prompt.
- [var metadata: [String : GeneratedContent]](transcript/prompt/metadata.md)
  Metadata provided as part of this prompt.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transcript.Entry](transcript/entry.md)
  An entry in a transcript.
- [Transcript.Instructions](transcript/instructions.md)
  Instructions you provide to the model that define its behavior.
- [Transcript.Response](transcript/response.md)
  A response from the model.
- [Transcript.Reasoning](transcript/reasoning.md)
  A reasoning entry from the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/prompt)*