# CFDictionaryRetainCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to retain a value or key being added to a dictionary.

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
typealias CFDictionaryRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

#### Return Value

The value or key to store in the dictionary, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in the collection.

#### Discussion

This callback is passed to [`CFDictionaryCreate(_:_:_:_:_:_:)`](cfdictionarycreate(_:_:_:_:_:_:).md) in a [`CFDictionaryKeyCallBacks`](cfdictionarykeycallbacks.md) and [`CFDictionaryValueCallBacks`](cfdictionaryvaluecallbacks.md) structure.

## Parameters

- `allocator`: The dictionary’s allocator.
- `value`: The value being added to the dictionary.

## See Also

- [typealias CFDictionaryApplierFunction](cfdictionaryapplierfunction.md)
  Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [typealias CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryEqualCallBack](cfdictionaryequalcallback.md)
  Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [typealias CFDictionaryHashCallBack](cfdictionaryhashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [typealias CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md)
  Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryretaincallback)*