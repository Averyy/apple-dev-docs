# CFDictionaryCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable dictionary with the key-value pairs from another dictionary.

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
func CFDictionaryCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theDict: CFDictionary!) -> CFMutableDictionary!
```

#### Return Value

A new dictionary that contains the same values as `theDict`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new dictionary and its storage for key-value pairs. Pass `NULL` or [`kCFAllocatorDefault`](kcfallocatordefault.md) to use the current default allocator.
- `capacity`: The maximum number of key-value pairs that can be contained by the new dictionary. The dictionary starts with the same number of key-value pairs as `theDict` and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theDict`.
- `theDict`: The dictionary to copy. The keys and values from the dictionary are copied as pointers into the new dictionary, not that which the values point to (if anything). The keys and values are also retained by the new dictionary. The count of the new dictionary is the same as the count of `theDict`. The new dictionary uses the same callbacks as `theDict`.

## See Also

- [func CFDictionaryCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>!, UnsafePointer<CFDictionaryValueCallBacks>!) -> CFMutableDictionary!](cfdictionarycreatemutable(_:_:_:_:).md)
  Creates a new mutable dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycreatemutablecopy(_:_:_:))*