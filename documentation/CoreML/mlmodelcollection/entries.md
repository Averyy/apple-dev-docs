# entries

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A dictionary of model entries keyed to the models’ identifiers.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
var entries: [String : MLModelCollection.Entry] { get }
```

```objc
@property (nonatomic, copy, readonly) NSDictionary<NSString *,MLModelCollectionEntry *> * entries;
```

## See Also

### Retreiving models from a collection
- [MLModelCollection.Entry](./entry.md)
  A model and its identifier within a model collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/entries)*