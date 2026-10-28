# ModelSampleInput

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

The data a language model receives for evaluation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct ModelSampleInput
```

## Overview

```swift
@Generable
struct WeatherAnswer {
    let condition: String
}

let input = ModelSampleInput(
    prompt: Prompt("What's the weather like in Cupertino?"),
    instructions: Instructions("Respond with the weather condition only."),
    generationSchema: GenerationSchema(type: WeatherAnswer.self, properties: [])
)
```

synthesizes text representations for display, logging, and synthetic data.

## Topics

### Initializers
- [init(prompt: Prompt, instructions: Instructions?, generationSchema: GenerationSchema?)](./modelsampleinput/init%28prompt,instructions,generationschema%29.md)
  Creates a model sample input with the given prompt, instructions, and schema.
### Instance Properties
- [var description: String](./modelsampleinput/description.md)
  A text representation of this input, equivalent to `promptDescription`.
- [var generationSchema: GenerationSchema?](./modelsampleinput/generationschema.md)
  The output schema for the assistant’s response.
- [var instructions: Instructions?](./modelsampleinput/instructions.md)
  The optional FoundationModels instructions for this input.
- [var instructionsDescription: String?](./modelsampleinput/instructionsdescription.md)
  A text representation of the instructions, synthesized from instruction segments.
- [var prompt: Prompt](./modelsampleinput/prompt.md)
  The FoundationModels prompt for this input.
- [var promptDescription: String](./modelsampleinput/promptdescription.md)
  A text representation of the prompt, synthesized from prompt segments.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bundled input and output
- [struct ModelSampleOutput](./modelsampleoutput.md)
  The expected output value and evaluation expectations for a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleinput)*