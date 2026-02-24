# CFDataCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFMutableData object by copying another CFData object.

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
func CFDataCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theData: CFData!) -> CFMutableData!
```

#### Return Value

A CFMutableData object that has the same contents as the original object. Returns `NULL` if there was a problem copying the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The CFAllocator object to be used to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `capacity`: The maximum number of bytes that the CFData object can contain. The CFData object starts with the same length as the original object, and can grow to contain this number of bytes. Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the length of `theData`.
- `theData`: The CFData object to be copied.

## See Also

- [func CFDataCreateMutable(CFAllocator!, CFIndex) -> CFMutableData!](cfdatacreatemutable(_:_:).md)
  Creates an empty CFMutableData object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreatemutablecopy(_:_:_:))*