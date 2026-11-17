# SystemLanguageModel.UseCase

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that represents the use case for prompting.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct UseCase
```

## Topics

### Getting the general use case
- [static let general: SystemLanguageModel.UseCase](./usecase/general.md)
  A use case for general prompting.
### Getting the content tagging use case
- [static let contentTagging: SystemLanguageModel.UseCase](./usecase/contenttagging.md)
  A use case for content tagging.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a model for a use case
- [convenience init(useCase: SystemLanguageModel.UseCase, guardrails: SystemLanguageModel.Guardrails)](./init%28usecase,guardrails%29.md)
  Creates a system language model instance for a specific use case.
- [SystemLanguageModel.Guardrails](./guardrails.md)
  A set of controls that flag sensitive content from model input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/usecase)*