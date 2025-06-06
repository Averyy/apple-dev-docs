# CFDictionaryHashCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.

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
typealias CFDictionaryHashCallBack = (UnsafeRawPointer?) -> CFHashCode
```

#### Return Value

An integer that can be used as a table address in a hash table structure.

#### Discussion

This callback is passed to [`CFDictionaryCreate(_:_:_:_:_:_:)`](cfdictionarycreate(_:_:_:_:_:_:).md) in a [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) structure.

## Parameters

- `value`: The value used to compute the hash code.

## See Also

- [typealias CFDictionaryApplierFunction](cfdictionaryapplierfunction.md)
  Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [typealias CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryEqualCallBack](cfdictionaryequalcallback.md)
  Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [typealias CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md)
  Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [typealias CFDictionaryRetainCallBack](cfdictionaryretaincallback.md)
  Prototype of a callback function used to retain a value or key being added to a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryhashcallback)*