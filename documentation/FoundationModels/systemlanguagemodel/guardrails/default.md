# default

**Framework**: Foundation Models  
**Kind**: property

Default guardrails. This mode ensures that unsafe content in prompts and responses will be blocked with a `LanguageModelSession.GenerationError.guardrailViolation` error.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let `default`: SystemLanguageModel.Guardrails
```

## See Also

- [static let permissiveContentTransformations: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/permissivecontenttransformations.md)
  Guardrails that allow for permissively transforming text input, including potentially unsafe content, to text responses, such as summarizing an article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/default)*