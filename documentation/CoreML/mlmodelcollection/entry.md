# MLModelCollection.Entry

**Framework**: Core ML  
**Kind**: class

A model and its identifier within a model collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class Entry
```

## Topics

### Identifying a model
- [var modelIdentifier: String](mlmodelcollection/entry/modelidentifier.md)
  The name of the model, which is unique to the collection.
### Locating a compiled model file
- [var modelURL: URL](mlmodelcollection/entry/modelurl.md)
  The compiled model’s location on the device’s file system.
### Comparing model collection entries
- [func isEqual(to: MLModelCollection.Entry) -> Bool](mlmodelcollection/entry/isequal(to:).md)
  Returns a Boolean value that indicates whether the two entries are equal.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var entries: [String : MLModelCollection.Entry]](mlmodelcollection/entries.md)
  A dictionary of model entries keyed to the models’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/entry)*