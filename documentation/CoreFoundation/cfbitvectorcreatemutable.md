# CFBitVectorCreateMutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a mutable bit vector.

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
func CFBitVectorCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex) -> CFMutableBitVector!
```

#### Return Value

A new bit vector. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `capacity`: Pass   to specify that the maximum capacity is not limited. The value must not be negative.

## See Also

- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.
- [func CFBitVectorCreateMutableCopy(CFAllocator!, CFIndex, CFBitVector!) -> CFMutableBitVector!](cfbitvectorcreatemutablecopy(_:_:_:).md)
  Creates a new mutable bit vector from a pre-existing bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatemutable(_:_:))*