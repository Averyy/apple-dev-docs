# CFDictionaryCreate(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable dictionary containing the specified key-value pairs.

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
func CFDictionaryCreate(_ allocator: CFAllocator!, _ keys: UnsafeMutablePointer<UnsafeRawPointer?>!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>!, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFDictionary!
```

#### Return Value

A new dictionary, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new dictionary. Pass   or   to use the current default allocator.
- `keys`: A C array of the pointer-sized keys to be in the new dictionary. This value may be   if the   parameter is  . This C array is not changed or freed by this function. The value must be a valid pointer to a C array of at least   pointers.
- `values`: A C array of the pointer-sized values to be in the new dictionary. This value may be   if the   parameter is  . This C array is not changed or freed by this function. The value must be a valid pointer to a C array of at least   elements.
- `numValues`: The number of key-value pairs to copy from the   and   C arrays into the new dictionary. This number will be the count of the dictionary; it must be non-negative and less than or equal to the actual number of keys or values.
- `keyCallBacks`: If the collection will contain CFType objects only, then pass a pointer to   as this parameter to use the default callback functions.
- `valueCallBacks`: If the collection will contain CFType objects only, then pass a pointer to   as this parameter to use the default callback functions.

## See Also

- [func CFDictionaryCreateCopy(CFAllocator!, CFDictionary!) -> CFDictionary!](cfdictionarycreatecopy(_:_:).md)
  Creates and returns a new immutable dictionary with the key-value pairs of another dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycreate(_:_:_:_:_:_:))*