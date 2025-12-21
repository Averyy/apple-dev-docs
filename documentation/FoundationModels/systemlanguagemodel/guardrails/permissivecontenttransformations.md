# permissiveContentTransformations

**Framework**: Foundation Models  
**Kind**: property

Guardrails that allow for permissively transforming text input, including potentially unsafe content, to text responses, such as summarizing an article.

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

In this mode, requests you make to the model that generate a `String` will not throw `LanguageModelSession.GenerationError.guardrailViolation` errors. However, when the purpose of your instructions and prompts is not transforming user input, the model may still refuse to respond to potentially unsafe prompts by generating an explanation.

When you generate responses other than `String`, this mode behaves the same way as `.default`.

## See Also

- [static let `default`: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/default.md)
  Default guardrails. This mode ensures that unsafe content in prompts and responses will be blocked with a `LanguageModelSession.GenerationError.guardrailViolation` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/permissivecontenttransformations)*