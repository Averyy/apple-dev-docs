# default

**Framework**: Foundation Models  
**Kind**: property

Guardrails that default to ensuring that the system blocks unsafe content in prompts and responses.

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

#### Discussion

When the framework blocks unsafe content it throws a [`LanguageModelSession.GenerationError.guardrailViolation(_:)`](languagemodelsession/generationerror/guardrailviolation(_:).md) error.

## See Also

- [static let permissiveContentTransformations: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/permissivecontenttransformations.md)
  Guardrails that allow for permissively transforming text input, including potentially unsafe content, to text responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/default)*