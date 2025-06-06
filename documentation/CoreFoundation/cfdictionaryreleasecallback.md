# CFDictionaryReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.

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
typealias CFDictionaryReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

## Parameters

- `allocator`: The dictionary’s allocator.
- `value`: The value being removed from the dictionary.

## See Also

- [typealias CFDictionaryApplierFunction](cfdictionaryapplierfunction.md)
  Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [typealias CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryEqualCallBack](cfdictionaryequalcallback.md)
  Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [typealias CFDictionaryHashCallBack](cfdictionaryhashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [typealias CFDictionaryRetainCallBack](cfdictionaryretaincallback.md)
  Prototype of a callback function used to retain a value or key being added to a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryreleasecallback)*