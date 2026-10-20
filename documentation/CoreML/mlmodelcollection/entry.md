# MLModelCollection.Entry

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A model and its identifier within a model collection.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
class Entry
```

```objc
@interface MLModelCollectionEntry : NSObject
```

## Topics

### Identifying a model
- [var modelIdentifier: String](./entry/modelidentifier.md)
  The name of the model, which is unique to the collection.
### Locating a compiled model file
- [var modelURL: URL](./entry/modelurl.md)
  The compiled model’s location on the device’s file system.
### Comparing model collection entries
- [func isEqual(to: MLModelCollection.Entry) -> Bool](./entry/isequal%28to%29.md)
  Returns a Boolean value that indicates whether the two entries are equal.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Retreiving models from a collection
- [var entries: [String : MLModelCollection.Entry]](./entries.md)
  A dictionary of model entries keyed to the models’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/entry)*