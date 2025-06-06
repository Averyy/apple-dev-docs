# CFAllocatorCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an allocator object.

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
func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!) -> Unmanaged<CFAllocator>!
```

#### Return Value

The new allocator object, or `NULL` if there was a problem allocating memory. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You use this function to create custom allocators which you can then pass into various Core Foundation object-creation functions. You must implement a function callback that allocates memory and assign it to the `allocate` field of this structure. You typically also implement deallocate, reallocate, and preferred-size callbacks.

## Parameters

- `allocator`: The existing allocator to use to allocate memory for the new allocator. Pass the   constant for this parameter to allocate memory using the appropriate function callback specified in the   parameter. Pass   or   to allocate memory for the new allocator using the default allocator.
- `context`: A structure of type  . The fields of this structure hold (among other things) function pointers to callbacks used for allocating, reallocating, and deallocating memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorcreate(_:_:))*