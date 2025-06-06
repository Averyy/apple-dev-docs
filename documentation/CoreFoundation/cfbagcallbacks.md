# CFBagCallBacks

**Framework**: Core Foundation  
**Kind**: struct

This structure contains the callbacks used to retain, release, describe, and compare the values of a CFBag object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFBagCallBacks
```

## Topics

### Initializers
- [init()](cfbagcallbacks/init.md)
- [init(version: CFIndex, retain: CFBagRetainCallBack!, release: CFBagReleaseCallBack!, copyDescription: CFBagCopyDescriptionCallBack!, equal: CFBagEqualCallBack!, hash: CFBagHashCallBack!)](cfbagcallbacks/init(version:retain:release:copydescription:equal:hash:).md)
### Instance Properties
- [var copyDescription: CFBagCopyDescriptionCallBack!](cfbagcallbacks/copydescription.md)
  The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [`CFBagCopyDescriptionCallBack`](cfbagcopydescriptioncallback.md) for a description of this callback.
- [var equal: CFBagEqualCallBack!](cfbagcallbacks/equal.md)
  The callback used to compare values in the collection for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [`CFBagEqualCallBack`](cfbagequalcallback.md) for a description of this callback.
- [var hash: CFBagHashCallBack!](cfbagcallbacks/hash.md)
  The callback used to compute a hash code for values in a collection. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [`CFBagHashCallBack`](cfbaghashcallback.md) for a description of this callback.
- [var release: CFBagReleaseCallBack!](cfbagcallbacks/release.md)
  The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [`CFBagReleaseCallBack`](cfbagreleasecallback.md) for a description of this callback.
- [var retain: CFBagRetainCallBack!](cfbagcallbacks/retain.md)
  The callback used to retain each value as they are added to the collection. If `NULL`, values are not retained. See [`CFBagRetainCallBack`](cfbagretaincallback.md) for a descriptions of this function’s parameters.
- [var version: CFIndex](cfbagcallbacks/version.md)
  The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks)*