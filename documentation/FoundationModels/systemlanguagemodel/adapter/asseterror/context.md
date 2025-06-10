# SystemLanguageModel.Adapter.AssetError.Context

**Framework**: Foundation Models  
**Kind**: struct

The context in which the error occurred.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Context
```

## Topics

### Creating a context
- [init(debugDescription: String, underlyingErrors: [any Error])](systemlanguagemodel/adapter/asseterror/context/init(debugdescription:underlyingerrors:).md)
### Getting the debug description
- [let debugDescription: String](systemlanguagemodel/adapter/asseterror/context/debugdescription.md)
  A debug description to help developers diagnose issues during development.
### Getting the underlying errors
- [let underlyingErrors: [any Error]](systemlanguagemodel/adapter/asseterror/context/underlyingerrors.md)
  The underlying errors that caused this error.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case compatibleAdapterNotFound(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/compatibleadapternotfound(_:).md)
  An error that happens if there are no compatible adapters for the current system base model.
- [case invalidAdapterName(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/invalidadaptername(_:).md)
  An error that happens if the provided adapter name is invalid.
- [case invalidAsset(SystemLanguageModel.Adapter.AssetError.Context)](systemlanguagemodel/adapter/asseterror/invalidasset(_:).md)
  An error that happens if the provided asset files are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/asseterror/context)*