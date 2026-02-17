# permissiveContentTransformations

**Framework**: Foundation Models  
**Kind**: property

Guardrails that allow for permissively transforming text input, including potentially unsafe content, to text responses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let permissiveContentTransformations: SystemLanguageModel.Guardrails
```

## Mentions

- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)

#### Discussion

In this mode, requests you make to the model that generate a string won’t throw [`LanguageModelSession.GenerationError.guardrailViolation(_:)`](languagemodelsession/generationerror/guardrailviolation(_:).md) errors. However, when the purpose of your instructions and prompts isn’t to transform input from a person, the model may still refuse to respond to potentially unsafe prompts by generating an explanation.

When you generate responses other than string, this mode behaves the same way as [`default`](systemlanguagemodel/guardrails/default.md).

## See Also

- [static let `default`: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/default.md)
  Guardrails that default to ensuring that the system blocks unsafe content in prompts and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/permissivecontenttransformations)*