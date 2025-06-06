# CFDictionaryValueCallBacks

**Framework**: Core Foundation  
**Kind**: struct

This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.

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
struct CFDictionaryValueCallBacks
```

## Topics

### Initializers
- [init()](cfdictionaryvaluecallbacks/init.md)
- [init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!)](cfdictionaryvaluecallbacks/init(version:retain:release:copydescription:equal:).md)
### Instance Properties
- [var copyDescription: CFDictionaryCopyDescriptionCallBack!](cfdictionaryvaluecallbacks/copydescription.md)
  The callback used to create a descriptive string representation of each value in the dictionary. If `NULL`, the collection will create a simple description of each value. See [`CFDictionaryCopyDescriptionCallBack`](cfdictionarycopydescriptioncallback.md) for a description of this callback.
- [var equal: CFDictionaryEqualCallBack!](cfdictionaryvaluecallbacks/equal.md)
  The callback used to compare values in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare values in the collection. See [`CFDictionaryEqualCallBack`](cfdictionaryequalcallback.md) for a description of this callback.
- [var release: CFDictionaryReleaseCallBack!](cfdictionaryvaluecallbacks/release.md)
  The callback used to release values as they are removed from the dictionary. If `NULL`, values are not released. See [`CFDictionaryReleaseCallBack`](cfdictionaryreleasecallback.md) for a description of this callback.
- [var retain: CFDictionaryRetainCallBack!](cfdictionaryvaluecallbacks/retain.md)
  The callback used to retain each value as they are added to the collection. This callback returns the value to use as the value in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the value. If `NULL`, values are not retained. See [`CFDictionaryRetainCallBack`](cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.
- [var version: CFIndex](cfdictionaryvaluecallbacks/version.md)
  The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks)*