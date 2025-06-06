# CFDictionaryCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates and returns a new immutable dictionary with the key-value pairs of another dictionary.

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
func CFDictionaryCreateCopy(_ allocator: CFAllocator!, _ theDict: CFDictionary!) -> CFDictionary!
```

#### Return Value

A new dictionary that contains the same key-value pairs as `theDict`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new dictionary. Pass   or   to use the current default allocator.
- `theDict`: The dictionary to copy. The keys and values from the dictionary are copied as pointers into the new dictionary. However, the keys and values are also retained by the new dictionary. The count of the new dictionary is the same as the count of  . The new dictionary uses the same callbacks as  .

## See Also

- [func CFDictionaryCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>!, UnsafePointer<CFDictionaryValueCallBacks>!) -> CFDictionary!](cfdictionarycreate(_:_:_:_:_:_:).md)
  Creates an immutable dictionary containing the specified key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycreatecopy(_:_:))*