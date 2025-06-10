# delete(model:where:includeSubclasses:)

**Framework**: SwiftData  
**Kind**: method

Removes each model satisfying the given predicate from the persistent storage during the next save operation.

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
func delete<T>(model: T.Type, where predicate: Predicate<T>? = nil, includeSubclasses: Bool = true) throws where T : PersistentModel
```

#### Discussion

> ⚠️ **Warning**: If you don’t provide a predicate, the context will remove all models of the specified type from the persistent storage.

## Parameters

- `model`: The type of the model to remove.
- `predicate`: The logical condition to use when determining if the context should remove a particular model. The default value is  .
- `includeSubclasses`: A Boolean value that indicates whether the context includes subclasses of the specified model type when evaluating models to remove. The default value is  .

## See Also

- [var deletedModelsArray: [any PersistentModel]](modelcontext/deletedmodelsarray.md)
  The array of registered models that the context will remove from the persistent storage during the next save operation.
- [func delete<T>(T)](modelcontext/delete(_:).md)
  Removes the specified model from the persistent storage during the next save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/delete(model:where:includesubclasses:))*