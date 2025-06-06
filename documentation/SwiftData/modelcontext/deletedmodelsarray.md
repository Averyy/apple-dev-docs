# deletedModelsArray

**Framework**: SwiftData  
**Kind**: property

The array of registered models that the context will remove from the persistent storage during the next save operation.

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
var deletedModelsArray: [any PersistentModel] { get }
```

## See Also

- [func delete<T>(T)](modelcontext/delete(_:).md)
  Removes the specified model from the persistent storage during the next save operation.
- [func delete<T>(model: T.Type, where: Predicate<T>?, includeSubclasses: Bool) throws](modelcontext/delete(model:where:includesubclasses:).md)
  Removes each model satisfying the given predicate from the persistent storage during the next save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/deletedmodelsarray)*