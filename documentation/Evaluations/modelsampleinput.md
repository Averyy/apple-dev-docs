# ModelSampleInput

**Framework**: Evaluations  
**Kind**: struct

The data sent to a language model for evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ModelSampleInput
```

#### Overview

Stores FoundationModels types (`Prompt`, `Instructions`) and automatically synthesizes text representations for display, logging, and synthetic data.

## Topics

### Initializers
- [init(prompt: Prompt, instructions: Instructions?, generationSchema: GenerationSchema?)](modelsampleinput/init(prompt:instructions:generationschema:).md)
  Creates a model sample input with the given prompt, instructions, and schema.
### Instance Properties
- [var generationSchema: GenerationSchema?](modelsampleinput/generationschema.md)
  The output schema for the assistant’s response.
- [var instructions: Instructions?](modelsampleinput/instructions.md)
  The optional FoundationModels instructions for this input.
- [var instructionsDescription: String?](modelsampleinput/instructionsdescription.md)
  A text representation of the instructions, synthesized from instruction segments.
- [var prompt: Prompt](modelsampleinput/prompt.md)
  The FoundationModels prompt for this input.
- [var promptDescription: String](modelsampleinput/promptdescription.md)
  A text representation of the prompt, synthesized from prompt segments.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ModelSampleOutput](modelsampleoutput.md)
  The expected output value and evaluation expectations for a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleinput)*