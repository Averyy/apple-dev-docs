# init(prompt:instructions:generationSchema:)

**Framework**: Evaluations  
**Kind**: init

Creates a model sample input with the given prompt, instructions, and schema.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(prompt: Prompt, instructions: Instructions? = nil, generationSchema: GenerationSchema? = nil)
```

## Parameters

- `prompt`: The prompt to send to the language model.
- `instructions`: Optional system instructions for the model session.
- `generationSchema`: The output schema for the assistant’s response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleinput/init(prompt:instructions:generationschema:))*