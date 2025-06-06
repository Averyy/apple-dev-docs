# CFBitVectorCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable bit vector from a block of memory.

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
func CFBitVectorCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBits: CFIndex) -> CFBitVector!
```

#### Return Value

A new bit vector. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bit vector. Pass   or kCFAllocatorDefault to use the current default allocator.
- `bytes`: A pointer to the bit values to store in the new bit vector. The values are copied into the bit vector’s own memory. The bit indices are numbered left-to-right with   being the left-most, or most-significant, bit in the byte stream.
- `numBits`: The number of bits in the bit vector.

## See Also

- [func CFBitVectorCreateCopy(CFAllocator!, CFBitVector!) -> CFBitVector!](cfbitvectorcreatecopy(_:_:).md)
  Creates an immutable bit vector that is a copy of another bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorcreate(_:_:_:))*