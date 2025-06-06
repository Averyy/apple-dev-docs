# CFArrayCallBacks

**Framework**: Core Foundation  
**Kind**: struct

Structure containing the callbacks of a CFArray.

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
struct CFArrayCallBacks
```

## Topics

### Initializers
- [init()](cfarraycallbacks/init.md)
- [init(version: CFIndex, retain: CFArrayRetainCallBack!, release: CFArrayReleaseCallBack!, copyDescription: CFArrayCopyDescriptionCallBack!, equal: CFArrayEqualCallBack!)](cfarraycallbacks/init(version:retain:release:copydescription:equal:).md)
### Instance Properties
- [var copyDescription: CFArrayCopyDescriptionCallBack!](cfarraycallbacks/copydescription.md)
  The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [`CFArrayCopyDescriptionCallBack`](cfarraycopydescriptioncallback.md) for a description of this callback.
- [var equal: CFArrayEqualCallBack!](cfarraycallbacks/equal.md)
  The callback used to compare values in the array for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [`CFArrayEqualCallBack`](cfarrayequalcallback.md) for a description of this callback.
- [var release: CFArrayReleaseCallBack!](cfarraycallbacks/release.md)
  The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [`CFArrayReleaseCallBack`](cfarrayreleasecallback.md) for a description of this callback.
- [var retain: CFArrayRetainCallBack!](cfarraycallbacks/retain.md)
  The callback used to retain each value as they are added to the collection. If `NULL`, values are not retained. See [`CFArrayRetainCallBack`](cfarrayretaincallback.md) for a description of this callback.
- [var version: CFIndex](cfarraycallbacks/version.md)
  The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks)*