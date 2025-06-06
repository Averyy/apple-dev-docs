# UnsafeBufferPointer

**Framework**: Swift  
**Kind**: struct

A nonowning collection interface to a buffer of elements stored contiguously in memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct UnsafeBufferPointer<Element> where Element : ~Copyable
```

#### Overview

You can use an `UnsafeBufferPointer` instance in low level operations to eliminate uniqueness checks and, in release mode, bounds checks. Bounds checks are always performed in debug mode.

### Unsafebufferpointer Semantics

An `UnsafeBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a value of type `UnsafeBufferPointer` does not copy the instances stored in the underlying memory. However, initializing another collection with an `UnsafeBufferPointer` instance copies the instances out of the referenced memory and into the new collection.

## Topics

### Initializers
- [init(MLMultiArray) throws](unsafebufferpointer/init(_:)-2fjdq.md)
- [init(UnsafeMutableBufferPointer<Element>)](unsafebufferpointer/init(_:)-36fvm.md)
  Creates an immutable typed buffer pointer referencing the same memory as the given mutable buffer pointer.
- [init(AudioBuffer)](unsafebufferpointer/init(_:)-5ei4s.md)
  Initialize an `UnsafeBufferPointer<Element>` from an `AudioBuffer`. Binds the buffer’s memory type to `Element`.
- [init(rebasing: Slice<UnsafeMutableBufferPointer<Element>>)](unsafebufferpointer/init(rebasing:)-53eec.md)
  Creates a buffer over the same memory as the given buffer slice.
- [init(rebasing: Slice<UnsafeBufferPointer<Element>>)](unsafebufferpointer/init(rebasing:)-56rdb.md)
  Creates a buffer over the same memory as the given buffer slice.
- [init(start: UnsafePointer<Element>?, count: Int)](unsafebufferpointer/init(start:count:).md)
  Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.
### Instance Properties
- [var baseAddress: UnsafePointer<Element>?](unsafebufferpointer/baseaddress.md)
  A pointer to the first element of the buffer.
- [let count: Int](unsafebufferpointer/count.md)
  The number of elements in the buffer.
### Instance Methods
- [func deallocate()](unsafebufferpointer/deallocate.md)
  Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [func extracting(some RangeExpression<Int>) -> UnsafeBufferPointer<Element>](unsafebufferpointer/extracting(_:)-47z4z.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func extracting((UnboundedRange_) -> ()) -> UnsafeBufferPointer<Element>](unsafebufferpointer/extracting(_:)-4bn8q.md)
  Extracts and returns a copy of the entire buffer.
- [func extracting(Range<Int>) -> UnsafeBufferPointer<Element>](unsafebufferpointer/extracting(_:)-nivx.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](unsafebufferpointer/withmemoryrebound(to:_:).md)
  Executes the given closure while temporarily binding the memory referenced by this buffer to the given type.
### Subscripts
- [subscript(Int) -> Element](unsafebufferpointer/subscript(_:)-3sy16.md)
  Accesses the element at the specified position.
### Default Implementations
- [AtomicRepresentable Implementations](unsafebufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafebufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafebufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafebufferpointer/customdebugstringconvertible-implementations.md)
- [Sequence Implementations](unsafebufferpointer/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/AccelerateBuffer.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sequence](sequence.md)

## See Also

- [struct UnsafePointer](unsafepointer.md)
  A pointer for accessing data of a specific type.
- [struct UnsafeMutablePointer](unsafemutablepointer.md)
  A pointer for accessing and manipulating data of a specific type.
- [struct UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
  A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer)*