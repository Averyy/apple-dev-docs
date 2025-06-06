# CFBitVectorCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable bit vector that is a copy of another bit vector.

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
func CFBitVectorCreateCopy(_ allocator: CFAllocator!, _ bv: CFBitVector!) -> CFBitVector!
```

#### Return Value

A new bit vector holding the same bit values as `bv`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bit vector. Pass   or kCFAllocatorDefault to use the current default allocator.
- `bv`: The bit vector to copy.

## See Also

- [func CFBitVectorCreate(CFAllocator!, UnsafePointer<UInt8>!, CFIndex) -> CFBitVector!](cfbitvectorcreate(_:_:_:).md)
  Creates an immutable bit vector from a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorcreatecopy(_:_:))*