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

The `permissiveContentTransform` guardrail model lets the model handle potentially unsafe content, such as summarizing a news article. In this mode, requests you make to the model that generate a `String` will not throw [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) errors. However, the model may still sometimes refuse to respond to a sensitive prompt, in which case it generates a `String` refusal message.

When you generate responses other than `String`, this mode behaves the same way as [`default`](systemlanguagemodel/guardrails/default.md) mode and throws [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) errors.

## See Also

- [static let `default`: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/default.md)
  Guardrails that default to ensuring that the system blocks unsafe content in prompts and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/permissivecontenttransformations)*