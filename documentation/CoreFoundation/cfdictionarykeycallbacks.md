# CFDictionaryKeyCallBacks

**Framework**: Core Foundation  
**Kind**: struct

This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.

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
struct CFDictionaryKeyCallBacks
```

## Topics

### Initializers
- [init()](cfdictionarykeycallbacks/init.md)
- [init(version: CFIndex, retain: CFDictionaryRetainCallBack!, release: CFDictionaryReleaseCallBack!, copyDescription: CFDictionaryCopyDescriptionCallBack!, equal: CFDictionaryEqualCallBack!, hash: CFDictionaryHashCallBack!)](cfdictionarykeycallbacks/init(version:retain:release:copydescription:equal:hash:).md)
### Instance Properties
- [var copyDescription: CFDictionaryCopyDescriptionCallBack!](cfdictionarykeycallbacks/copydescription.md)
  The callback used to create a descriptive string representation of each key in the dictionary. If `NULL`, the collection will create a simple description of each key. See [`CFDictionaryCopyDescriptionCallBack`](cfdictionarycopydescriptioncallback.md) for a description of this callback.
- [var equal: CFDictionaryEqualCallBack!](cfdictionarykeycallbacks/equal.md)
  The callback used to compare keys in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare keys in the collection. See [`CFDictionaryEqualCallBack`](cfdictionaryequalcallback.md) for a description of this callback.
- [var hash: CFDictionaryHashCallBack!](cfdictionarykeycallbacks/hash.md)
  The callback used to compute a hash code for keys as they are used to access, add, or remove values in the dictionary. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [`CFDictionaryHashCallBack`](cfdictionaryhashcallback.md) for a description of this callback.
- [var release: CFDictionaryReleaseCallBack!](cfdictionarykeycallbacks/release.md)
  The callback used to release keys as they are removed from the dictionary. If `NULL`, keys are not released. See [`CFDictionaryReleaseCallBack`](cfdictionaryreleasecallback.md) for a description of this callback.
- [var retain: CFDictionaryRetainCallBack!](cfdictionarykeycallbacks/retain.md)
  The callback used to retain each key as they are added to the collection. This callback returns the value to use as the key in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the key. If `NULL`, keys are not retained. See [`CFDictionaryRetainCallBack`](cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.
- [var version: CFIndex](cfdictionarykeycallbacks/version.md)
  The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks)*