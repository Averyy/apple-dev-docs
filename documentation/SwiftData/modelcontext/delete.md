# delete(_:)

**Framework**: SwiftData  
**Kind**: method

Removes the specified model from the persistent storage during the next save operation.

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
func delete<T>(_ model: T) where T : PersistentModel
```

#### Discussion

When the context nexts commits its changes, SwiftData removes the model from the persistent storage. If the model is new and in an unsaved state, the context simply discards it.

## Parameters

- `model`: The persistent model to delete.

## See Also

- [var deletedModelsArray: [any PersistentModel]](modelcontext/deletedmodelsarray.md)
  The array of registered models that the context will remove from the persistent storage during the next save operation.
- [func delete<T>(model: T.Type, where: Predicate<T>?, includeSubclasses: Bool) throws](modelcontext/delete(model:where:includesubclasses:).md)
  Removes each model satisfying the given predicate from the persistent storage during the next save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/delete(_:))*