# CFDataCreateMutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an empty CFMutableData object.

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
func CFDataCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex) -> CFMutableData!
```

#### Return Value

A CFMutableData object or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates an empty (that is, content-less) CFMutableData object. You can add raw data to this object with the [`CFDataAppendBytes(_:_:_:)`](cfdataappendbytes(_:_:_:).md) function, and thereafter you can replace and delete characters with the appropriate CFMutableData functions. If the `capacity` parameter is greater than `0`, any attempt to add characters beyond this limit can result in undefined behavior.

## Parameters

- `allocator`: The CFAllocator object to be used to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `capacity`: Pass   to specify that the maximum capacity is not limited. The value must not be negative.

## See Also

- [func CFDataCreateMutableCopy(CFAllocator!, CFIndex, CFData!) -> CFMutableData!](cfdatacreatemutablecopy(_:_:_:).md)
  Creates a CFMutableData object by copying another CFData object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreatemutable(_:_:))*