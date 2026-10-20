# CFDictionaryEqualCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Prototype of a callback function used to determine if two values or keys in a dictionary are equal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFDictionaryEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean
```

```c
typedef unsigned char (*)(const void *, const void *) CFDictionaryEqualCallBack;
```

#### Discussion

This callback is passed to [`CFDictionaryCreate(_:_:_:_:_:_:)`](./cfdictionarycreate%28_,_,_,_,_,_%29.md) in a [`CFDictionaryKeyCallBacks`](./cfdictionarykeycallbacks.md) and [`CFDictionaryValueCallBacks`](./cfdictionaryvaluecallbacks.md) structure.

## Parameters

- `value1`: A value in the dictionary.
- `value2`: Another value in the dictionary.

## See Also

### Callbacks
- [typealias CFDictionaryApplierFunction](./cfdictionaryapplierfunction.md)
  Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [typealias CFDictionaryCopyDescriptionCallBack](./cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryHashCallBack](./cfdictionaryhashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [typealias CFDictionaryReleaseCallBack](./cfdictionaryreleasecallback.md)
  Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [typealias CFDictionaryRetainCallBack](./cfdictionaryretaincallback.md)
  Prototype of a callback function used to retain a value or key being added to a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryequalcallback)*