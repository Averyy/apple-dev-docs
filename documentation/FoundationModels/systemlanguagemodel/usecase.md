# SystemLanguageModel.UseCase

**Framework**: Foundation Models  
**Kind**: struct

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
- [static let general: SystemLanguageModel.UseCase](systemlanguagemodel/usecase/general.md)
  A use case for general prompting.
### Getting the content tagging use case
- [static let contentTagging: SystemLanguageModel.UseCase](systemlanguagemodel/usecase/contenttagging.md)
  A use case for content tagging.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(useCase: SystemLanguageModel.UseCase, guardrails: SystemLanguageModel.Guardrails)](systemlanguagemodel/init(usecase:guardrails:).md)
  Creates a system language model instance for a specific use case.
- [SystemLanguageModel.Guardrails](systemlanguagemodel/guardrails.md)
  A set of controls that flag sensitive content from model input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/usecase)*