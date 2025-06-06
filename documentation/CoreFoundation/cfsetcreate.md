# CFSetCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable CFSet object containing supplied values.

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
func CFSetCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFSetCallBacks>!) -> CFSet!
```

#### Return Value

A new immutable set, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new set and its storage for values. Pass   or   to use the current default allocator.
- `values`: A C array of the pointer-sized values to be in the new set. This parameter may be   if the   parameter is 0. The C array is not changed or freed by this function.   must be a pointer to a C array of at least   elements.
- `numValues`: The number of values to copy from the   C array in the new set.
- `callBacks`: This value may be  , which is treated as a valid structure of version   with all fields  . If the collection contains only CFType objects, then pass   to use the default callback functions.

## See Also

- [func CFSetCreateCopy(CFAllocator!, CFSet!) -> CFSet!](cfsetcreatecopy(_:_:).md)
  Creates an immutable set containing the values of an existing set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcreate(_:_:_:_:))*