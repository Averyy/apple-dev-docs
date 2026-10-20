# prompt

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

The user’s prompt for this sample.

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
var prompt: Prompt { get }
```

Available when `ExpectedValue` conforms to `Decodable`, `Encodable`, and `Sendable`.

## Mentions

- [Evaluating language model responses](../evaluating-language-model-responses.md)

## See Also

### Specifying the query
- [var promptDescription: String](./promptdescription.md)
  A text representation of the prompt, synthesized from its segments.
- [var instructions: Instructions?](./instructions.md)
  Optional instructions providing context to the model for this sample.
- [var instructionsDescription: String?](./instructionsdescription.md)
  A text representation of the instructions, synthesized from their segments.
- [var input: ModelSampleInput](./input.md)
  The bundled language model input (prompt, instructions, schema).


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample/prompt)*