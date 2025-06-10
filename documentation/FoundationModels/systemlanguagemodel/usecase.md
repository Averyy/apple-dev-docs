# SystemLanguageModel.UseCase

**Framework**: Foundation Models  
**Kind**: struct

A type that represents the use case for prompting.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct UseCase
```

## Topics

### Getting the use cases
- [static let general: SystemLanguageModel.UseCase](systemlanguagemodel/usecase/general.md)
  A use case for general prompting.
- [static let contentTagging: SystemLanguageModel.UseCase](systemlanguagemodel/usecase/contenttagging.md)
  A use case for content tagging.
### Comparing use cases
- [static func == (SystemLanguageModel.UseCase, SystemLanguageModel.UseCase) -> Bool](systemlanguagemodel/usecase/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](systemlanguagemodel/usecase/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
  Enhance the experience in your app by prompting an on-device large language model.
- [Improving safety from generative model output](improving-safety-from-generative-model-output.md)
  Create generative experiences that appropriately handle sensitive inputs and respect people.
- [Adding intelligent app features with generative models](adding-intelligent-app-features-with-generative-models.md)
  Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.
- [class SystemLanguageModel](systemlanguagemodel.md)
  An on-device large language model capable of text generation tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/usecase)*