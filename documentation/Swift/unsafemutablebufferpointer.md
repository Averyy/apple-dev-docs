# UnsafeMutableBufferPointer

**Framework**: Swift  
**Kind**: struct

A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.

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
struct UnsafeMutableBufferPointer<Element> where Element : ~Copyable
```

#### Overview

You can use an `UnsafeMutableBufferPointer` instance in low level operations to eliminate uniqueness checks and, in release mode, bounds checks. Bounds checks are always performed in debug mode.

### Unsafemutablebufferpointer Semantics

An `UnsafeMutableBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a value of type `UnsafeMutableBufferPointer` does not copy the instances stored in the underlying memory. However, initializing another collection with an `UnsafeMutableBufferPointer` instance copies the instances out of the referenced memory and into the new collection.

## Topics

### Initializers
- [init(AudioBuffer)](unsafemutablebufferpointer/init(_:)-6750l.md)
  Initialize an `UnsafeMutableBufferPointer<Element>` from an `AudioBuffer`.
- [init(MLMultiArray) throws](unsafemutablebufferpointer/init(_:)-789ap.md)
- [init(mutating: UnsafeBufferPointer<Element>)](unsafemutablebufferpointer/init(mutating:).md)
  Creates a mutable typed buffer pointer referencing the same memory as the given immutable buffer pointer.
- [init(rebasing: Slice<UnsafeMutableBufferPointer<Element>>)](unsafemutablebufferpointer/init(rebasing:).md)
  Creates a buffer over the same memory as the given buffer slice.
- [init(start: UnsafeMutablePointer<Element>?, count: Int)](unsafemutablebufferpointer/init(start:count:).md)
  Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.
### Instance Properties
- [var baseAddress: UnsafeMutablePointer<Element>?](unsafemutablebufferpointer/baseaddress.md)
  A pointer to the first element of the buffer.
- [let count: Int](unsafemutablebufferpointer/count.md)
  The number of elements in the buffer.
- [var mutableSpan: MutableSpan<Element>](unsafemutablebufferpointer/mutablespan.md)
- [var span: Span<Element>](unsafemutablebufferpointer/span.md)
### Instance Methods
- [func assign(repeating: Element)](unsafemutablebufferpointer/assign(repeating:).md)
- [func deallocate()](unsafemutablebufferpointer/deallocate.md)
  Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [func deinitialize() -> UnsafeMutableRawBufferPointer](unsafemutablebufferpointer/deinitialize.md)
  Deinitializes every instance in this buffer.
- [func deinitializeElement(at: UnsafeMutableBufferPointer<Element>.Index)](unsafemutablebufferpointer/deinitializeelement(at:).md)
  Deinitializes the memory underlying the element at `index`.
- [func extracting(Range<Int>) -> UnsafeMutableBufferPointer<Element>](unsafemutablebufferpointer/extracting(_:)-4izct.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func extracting(some RangeExpression<Int>) -> UnsafeMutableBufferPointer<Element>](unsafemutablebufferpointer/extracting(_:)-51ps5.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func extracting((UnboundedRange_) -> ()) -> UnsafeMutableBufferPointer<Element>](unsafemutablebufferpointer/extracting(_:)-6xfww.md)
  Extracts and returns a copy of the entire buffer.
- [func initialize<S>(from: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index)](unsafemutablebufferpointer/initialize(from:).md)
  Initializes the buffer’s memory with the given elements.
- [func initialize(fromContentsOf: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/initialize(fromcontentsof:).md)
  Initializes the buffer’s memory with every element of the source.
- [func initialize(repeating: Element)](unsafemutablebufferpointer/initialize(repeating:).md)
  Initializes every element in this buffer’s memory to a copy of the given value.
- [func initializeElement(at: UnsafeMutableBufferPointer<Element>.Index, to: consuming Element)](unsafemutablebufferpointer/initializeelement(at:to:).md)
  Initializes the element at `index` to the given value.
- [func moveElement(from: UnsafeMutableBufferPointer<Element>.Index) -> Element](unsafemutablebufferpointer/moveelement(from:).md)
  Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.
- [func moveInitialize(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/moveinitialize(fromcontentsof:)-1ag7a.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func moveInitialize(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/moveinitialize(fromcontentsof:)-8aiwj.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func moveUpdate(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/moveupdate(fromcontentsof:)-4bpe7.md)
  Updates this buffer’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.
- [func moveUpdate(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/moveupdate(fromcontentsof:)-522y2.md)
  Updates this buffer’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.
- [func update<S>(from: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index)](unsafemutablebufferpointer/update(from:).md)
  Updates the buffer’s initialized memory with the given elements.
- [func update(fromContentsOf: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index](unsafemutablebufferpointer/update(fromcontentsof:).md)
  Updates the buffer’s initialized memory with every element of the source.
- [func update(repeating: Element)](unsafemutablebufferpointer/update(repeating:).md)
  Updates every element of this buffer’s initialized memory.
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeMutableBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](unsafemutablebufferpointer/withmemoryrebound(to:_:).md)
  Executes the given closure while temporarily binding the memory referenced by this buffer to the given type.
### Subscripts
- [subscript(Int) -> Element](unsafemutablebufferpointer/subscript(_:)-2vl82.md)
  Accesses the element at the specified position.
### Type Methods
- [static func allocate(capacity: Int) -> UnsafeMutableBufferPointer<Element>](unsafemutablebufferpointer/allocate(capacity:).md)
  Allocates uninitialized memory for the specified number of instances of type `Element`.
### Default Implementations
- [AtomicRepresentable Implementations](unsafemutablebufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafemutablebufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafemutablebufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafemutablebufferpointer/customdebugstringconvertible-implementations.md)
- [MutableCollection Implementations](unsafemutablebufferpointer/mutablecollection-implementations.md)
- [OperationParameter Implementations](unsafemutablebufferpointer/operationparameter-implementations.md)
- [Sequence Implementations](unsafemutablebufferpointer/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/AccelerateBuffer.md)
- [AccelerateMutableBuffer](../Accelerate/AccelerateMutableBuffer.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BNNSGraph.Builder.OperationParameter](../Accelerate/BNNSGraph/Builder/OperationParameter.md)
- [BNNSGraph.PointerArgument](../Accelerate/BNNSGraph/PointerArgument.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [MutableCollection](mutablecollection.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sequence](sequence.md)

## See Also

- [struct UnsafePointer](unsafepointer.md)
  A pointer for accessing data of a specific type.
- [struct UnsafeMutablePointer](unsafemutablepointer.md)
  A pointer for accessing and manipulating data of a specific type.
- [struct UnsafeBufferPointer](unsafebufferpointer.md)
  A nonowning collection interface to a buffer of elements stored contiguously in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer)*