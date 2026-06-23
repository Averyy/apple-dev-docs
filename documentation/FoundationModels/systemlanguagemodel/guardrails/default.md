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
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let `default`: SystemLanguageModel.Guardrails
```

#### Discussion

The `default` guardrail level means that all guardrails are turned on. When the guardrails block unsafe content from either the prompt input or model response, the framework throws a [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) error.

## See Also

- [static let permissiveContentTransformations: SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails/permissivecontenttransformations.md)
  Guardrails that allow for permissively transforming text input, including potentially unsafe content, to text responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails/default)*