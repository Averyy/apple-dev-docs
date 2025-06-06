# CFBagCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable bag containing specified values.

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
func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>!) -> CFBag!
```

#### Return Value

A new bag, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bag and its storage for values. Pass   or kCFAllocatorDefault to use the current default allocator.
- `values`: A C array of the pointer-sized values to be in the new bag. This parameter may be   if the   parameter is 0. The C array is not changed or freed by this function.   must be a valid pointer to a C array of at least   elements.
- `numValues`: The number of values to copy from the   C array in the new CFBag object. If the number is negative or is greater than the actual number of values, the behavior is undefined.
- `callBacks`: A pointer to a   structure initialized with the callbacks to use to retain, release, describe, and compare values in the bag. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple collection creations. This parameter may be  , which is treated as if a valid structure of version 0 with all fields   had been passed in. Otherwise, if any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a   structure, the behavior is undefined. If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined. If the collection contains CFType objects only, then pass   as this parameter to use the default callback functions.

## See Also

- [func CFBagCreateCopy(CFAllocator!, CFBag!) -> CFBag!](cfbagcreatecopy(_:_:).md)
  Creates an immutable bag with the values of another bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcreate(_:_:_:_:))*