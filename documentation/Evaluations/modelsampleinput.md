# ModelSampleInput

**Framework**: Evaluations  
**Kind**: struct

The data a language model receives for evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
struct ModelSampleInput
```

#### Overview

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
- [init(prompt: Prompt, instructions: Instructions?, generationSchema: GenerationSchema?)](modelsampleinput/init(prompt:instructions:generationschema:).md)
  Creates a model sample input with the given prompt, instructions, and schema.
### Instance Properties
- [var description: String](modelsampleinput/description.md)
  A text representation of this input, equivalent to `promptDescription`.
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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ModelSampleOutput](modelsampleoutput.md)
  The expected output value and evaluation expectations for a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleinput)*