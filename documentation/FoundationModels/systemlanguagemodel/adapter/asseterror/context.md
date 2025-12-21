# SystemLanguageModel.Adapter.AssetError.Context

**Framework**: Foundation Models  
**Kind**: struct

The context in which the error occurred.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Context
```

## Topics

### Creating a context
- [init(debugDescription: String)](systemlanguagemodel/adapter/asseterror/context/init(debugdescription:).md)
### Getting the debug description
- [let debugDescription: String](systemlanguagemodel/adapter/asseterror/context/debugdescription.md)
  A debug description to help developers diagnose issues during development.

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