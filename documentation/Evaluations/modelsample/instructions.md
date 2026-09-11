# instructions

**Framework**: Evaluations  
**Kind**: property

Optional instructions providing context to the model for this sample.

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
var instructions: Instructions? { get }
```

## See Also

- [var prompt: Prompt](modelsample/prompt.md)
  The user’s prompt for this sample.
- [var promptDescription: String](modelsample/promptdescription.md)
  A text representation of the prompt, synthesized from its segments.
- [var instructionsDescription: String?](modelsample/instructionsdescription.md)
  A text representation of the instructions, synthesized from their segments.
- [var input: ModelSampleInput](modelsample/input.md)
  The bundled language model input (prompt, instructions, schema).


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/instructions)*