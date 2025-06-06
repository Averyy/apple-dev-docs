# CFDictionaryApplierFunction

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function that may be applied to every key-value pair in a dictionary.

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
typealias CFDictionaryApplierFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This callback is passed to the [`CFDictionaryApplyFunction(_:_:_:)`](cfdictionaryapplyfunction(_:_:_:).md) function which iterates over the key-value pairs in a dictionary and applies the behavior defined in the applier function to each key-value pair in a dictionary.

## Parameters

- `key`: The key associated with the current key-value pair.
- `value`: The value associated with the current key-value pair.
- `context`: The program-defined context parameter given to the apply   function.

## See Also

- [typealias CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryEqualCallBack](cfdictionaryequalcallback.md)
  Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [typealias CFDictionaryHashCallBack](cfdictionaryhashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [typealias CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md)
  Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [typealias CFDictionaryRetainCallBack](cfdictionaryretaincallback.md)
  Prototype of a callback function used to retain a value or key being added to a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryapplierfunction)*