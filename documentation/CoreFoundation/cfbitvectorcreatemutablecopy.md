# CFBitVectorCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable bit vector from a pre-existing bit vector.

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
func CFBitVectorCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ bv: CFBitVector!) -> CFMutableBitVector!
```

#### Return Value

A new bit vector holding the same bit values as `bv`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029)

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `capacity`: Pass   to specify that the maximum capacity is not limited. If non- ,   must be large enough to hold all bit values from  .
- `bv`: The bit vector to copy.

## See Also

- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.
- [func CFBitVectorCreateMutable(CFAllocator!, CFIndex) -> CFMutableBitVector!](cfbitvectorcreatemutable(_:_:).md)
  Creates a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatemutablecopy(_:_:_:))*