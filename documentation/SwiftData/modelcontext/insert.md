# insert(_:)

**Framework**: SwiftData  
**Kind**: method

Registers the specified model with the context so it can include the model in the next save operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
func insert<T>(_ model: T) where T : PersistentModel
```

#### Discussion

A model is given a temporary persistent identifier until the first time a context saves it, after which that context assigns a permanent identifier. If you call [`rollback()`](modelcontext/rollback().md) after inserting a model but before the next save operation, the context discards that model.

## Parameters

- `model`: The model to include in the next save operation.

## See Also

- [var insertedModelsArray: [any PersistentModel]](modelcontext/insertedmodelsarray.md)
  The array of inserted models that the context is yet to persist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/insert(_:))*