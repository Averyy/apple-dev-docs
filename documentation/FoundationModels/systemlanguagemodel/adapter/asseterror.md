# SystemLanguageModel.Adapter.AssetError

**Framework**: Foundation Models  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum AssetError
```

## Topics

### Getting the asset errors
- [case compatibleAdapterNotFound(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/compatibleadapternotfound(_:).md)
  An error that happens if there are no compatible adapters for the current system base model.
- [case invalidAdapterName(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/invalidadaptername(_:).md)
  An error that happens if the provided adapter name is invalid.
- [case invalidAsset(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/invalidasset(_:).md)
  An error that happens if the provided asset files are invalid.
- [SystemLanguageModel.Adapter.AssetError.Context](systemlanguagemodel/adapter/asseterror/context.md)
  The context in which the error occurred.
### Getting the error description
- [var errorDescription: String](systemlanguagemodel/adapter/asseterror/errordescription.md)
  A string representation of the error description.
### Getting the recovery suggestion
- [var recoverySuggestion: String?](systemlanguagemodel/adapter/asseterror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
### Default Implementations
- [Error Implementations](systemlanguagemodel/adapter/asseterror/error-implementations.md)
- [LocalizedError Implementations](systemlanguagemodel/adapter/asseterror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/asseterror)*