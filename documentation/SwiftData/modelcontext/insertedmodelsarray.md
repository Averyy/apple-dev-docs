# insertedModelsArray

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The array of inserted models that the context is yet to persist.

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
var insertedModelsArray: [any PersistentModel] { get }
```

## See Also

### Inserting models
- [func insert<T>(T)](./insert%28_%29.md)
  Registers the specified model with the context so it can include the model in the next save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/insertedmodelsarray)*