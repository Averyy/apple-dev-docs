# promptDescription

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

A text representation of the prompt, synthesized from its segments.

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
var promptDescription: String { get }
```

Available when `ExpectedValue` conforms to `Decodable`, `Encodable`, and `Sendable`.

## See Also

### Specifying the query
- [var prompt: Prompt](./prompt.md)
  The user’s prompt for this sample.
- [var instructions: Instructions?](./instructions.md)
  Optional instructions providing context to the model for this sample.
- [var instructionsDescription: String?](./instructionsdescription.md)
  A text representation of the instructions, synthesized from their segments.
- [var input: ModelSampleInput](./input.md)
  The bundled language model input (prompt, instructions, schema).


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/promptdescription)*