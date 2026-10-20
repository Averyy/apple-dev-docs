# CFDataCreateMutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an empty CFMutableData object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDataCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex) -> CFMutableData!
```

```c
extern CFMutableDataRefCFDataCreateMutable(CFAllocatorRef allocator, CFIndex capacity);
```

#### Return Value

A CFMutableData object or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates an empty (that is, content-less) CFMutableData object. You can add raw data to this object with the [`CFDataAppendBytes(_:_:_:)`](./cfdataappendbytes%28_,_,_%29.md) function, and thereafter you can replace and delete characters with the appropriate CFMutableData functions. If the `capacity` parameter is greater than `0`, any attempt to add characters beyond this limit can result in undefined behavior.

## Parameters

- `allocator`: The CFAllocator object to be used to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `capacity`: The maximum number of bytes that the CFData object can contain. The CFData object starts empty and can grow to contain this number of values (and it can have less).

  Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.

## See Also

### Creating a Mutable Data Object
- [func CFDataCreateMutableCopy(CFAllocator!, CFIndex, CFData!) -> CFMutableData!](./cfdatacreatemutablecopy%28_,_,_%29.md)
  Creates a CFMutableData object by copying another CFData object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreatemutable(_:_:))*