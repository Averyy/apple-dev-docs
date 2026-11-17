# init(useCase:guardrails:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a system language model instance for a specific use case.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(useCase: SystemLanguageModel.UseCase = .general, guardrails: SystemLanguageModel.Guardrails = Guardrails.default)
```

## See Also

### Creating a model for a use case
- [SystemLanguageModel.UseCase](./usecase.md)
  A type that represents the use case for prompting.
- [SystemLanguageModel.Guardrails](./guardrails.md)
  A set of controls that flag sensitive content from model input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/init(usecase:guardrails:))*