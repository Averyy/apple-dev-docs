# CFDictionaryCreateMutable(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable dictionary.

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
func CFDictionaryCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ keyCallBacks: UnsafePointer<CFDictionaryKeyCallBacks>!, _ valueCallBacks: UnsafePointer<CFDictionaryValueCallBacks>!) -> CFMutableDictionary!
```

#### Return Value

A new dictionary, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new dictionary and its storage for key-value pairs. Pass   or   to use the current default allocator.
- `capacity`: Pass   to specify that the maximum capacity is not limited. The value must not be negative.
- `keyCallBacks`: If the dictionary will contain only CFType objects, then pass a pointer to   as this parameter to use the default callback functions.
- `valueCallBacks`: If the dictionary will contain CFType objects only, then pass a pointer to   as this parameter to use the default callback functions.

## See Also

- [func CFDictionaryCreateMutableCopy(CFAllocator!, CFIndex, CFDictionary!) -> CFMutableDictionary!](cfdictionarycreatemutablecopy(_:_:_:).md)
  Creates a new mutable dictionary with the key-value pairs from another dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycreatemutable(_:_:_:_:))*