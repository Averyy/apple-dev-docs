# UnsafeMutableBufferPointer

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

### UnsafeMutableBufferPointer Semantics

An `UnsafeMutableBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a value of type `UnsafeMutableBufferPointer` does not copy the instances stored in the underlying memory. However, initializing another collection with an `UnsafeMutableBufferPointer` instance copies the instances out of the referenced memory and into the new collection.

## Topics

### Initializers
- [init(AudioBuffer)](./unsafemutablebufferpointer/init%28_%29-6750l.md)
  Initialize an `UnsafeMutableBufferPointer<Element>` from an `AudioBuffer`.
- [init(MLMultiArray) throws](./unsafemutablebufferpointer/init%28_%29-789ap.md)
- [init(mutating: UnsafeBufferPointer<Element>)](./unsafemutablebufferpointer/init%28mutating%29.md)
  Creates a mutable typed buffer pointer referencing the same memory as the given immutable buffer pointer.
- [init(rebasing: Slice<UnsafeMutableBufferPointer<Element>>)](./unsafemutablebufferpointer/init%28rebasing%29.md)
  Creates a buffer over the same memory as the given buffer slice.
- [init(start: UnsafeMutablePointer<Element>?, count: Int)](./unsafemutablebufferpointer/init%28start,count%29.md)
  Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.
### Instance Properties
- [var baseAddress: UnsafeMutablePointer<Element>?](./unsafemutablebufferpointer/baseaddress.md)
  A pointer to the first element of the buffer.
- [let count: Int](./unsafemutablebufferpointer/count.md)
  The number of elements in the buffer.
- [var mutableSpan: MutableSpan<Element>](./unsafemutablebufferpointer/mutablespan.md)
  A mutable span over the elements of this buffer.
- [var span: Span<Element>](./unsafemutablebufferpointer/span.md)
  A span over the elements of this buffer.
### Instance Methods
- [func assign(repeating: Element)](./unsafemutablebufferpointer/assign%28repeating%29.md)
- [func deallocate()](./unsafemutablebufferpointer/deallocate%28%29.md)
  Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [func deinitialize() -> UnsafeMutableRawBufferPointer](./unsafemutablebufferpointer/deinitialize%28%29.md)
  Deinitializes every instance in this buffer.
- [func deinitializeElement(at: UnsafeMutableBufferPointer<Element>.Index)](./unsafemutablebufferpointer/deinitializeelement%28at%29.md)
  Deinitializes the memory underlying the element at `index`.
- [func extracting(Range<Int>) -> UnsafeMutableBufferPointer<Element>](./unsafemutablebufferpointer/extracting%28_%29-4izct.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func extracting(some RangeExpression<Int>) -> UnsafeMutableBufferPointer<Element>](./unsafemutablebufferpointer/extracting%28_%29-51ps5.md)
  Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [func extracting(UnboundedRange) -> UnsafeMutableBufferPointer<Element>](./unsafemutablebufferpointer/extracting%28_%29-6xfww.md)
  Extracts and returns a copy of the entire buffer.
- [func initialize<S>(from: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index)](./unsafemutablebufferpointer/initialize%28from%29.md)
  Initializes the buffer’s memory with the given elements.
- [func initialize(fromContentsOf: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/initialize%28fromcontentsof%29.md)
  Initializes the buffer’s memory with every element of the source.
- [func initialize(repeating: Element)](./unsafemutablebufferpointer/initialize%28repeating%29.md)
  Initializes every element in this buffer’s memory to a copy of the given value.
- [func initializeElement(at: UnsafeMutableBufferPointer<Element>.Index, to: consuming Element)](./unsafemutablebufferpointer/initializeelement%28at,to%29.md)
  Initializes the element at `index` to the given value.
- [func isTriviallyIdentical(to: UnsafeMutableBufferPointer<Element>) -> Bool](./unsafemutablebufferpointer/istriviallyidentical%28to%29.md)
  Returns a Boolean value indicating whether two instances refer to the same memory region.
- [func moveElement(from: UnsafeMutableBufferPointer<Element>.Index) -> Element](./unsafemutablebufferpointer/moveelement%28from%29.md)
  Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.
- [func moveInitialize(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/moveinitialize%28fromcontentsof%29-1ag7a.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func moveInitialize(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/moveinitialize%28fromcontentsof%29-8aiwj.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func moveUpdate(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/moveupdate%28fromcontentsof%29-4bpe7.md)
  Updates this buffer’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.
- [func moveUpdate(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/moveupdate%28fromcontentsof%29-522y2.md)
  Updates this buffer’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.
- [func update<S>(from: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index)](./unsafemutablebufferpointer/update%28from%29.md)
  Updates the buffer’s initialized memory with the given elements.
- [func update(fromContentsOf: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index](./unsafemutablebufferpointer/update%28fromcontentsof%29.md)
  Updates the buffer’s initialized memory with every element of the source.
- [func update(repeating: Element)](./unsafemutablebufferpointer/update%28repeating%29.md)
  Updates every element of this buffer’s initialized memory.
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeMutableBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](./unsafemutablebufferpointer/withmemoryrebound%28to,_%29.md)
  Executes the given closure while temporarily binding the memory referenced by this buffer to the given type.
### Subscripts
- [subscript(Int) -> Element](./unsafemutablebufferpointer/subscript%28_%29-2vl82.md)
  Accesses the element at the specified position.
### Type Methods
- [static func allocate(capacity: Int) -> UnsafeMutableBufferPointer<Element>](./unsafemutablebufferpointer/allocate%28capacity%29.md)
  Allocates uninitialized memory for the specified number of instances of type `Element`.
### Default Implementations
- [AtomicRepresentable Implementations](./unsafemutablebufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](./unsafemutablebufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](./unsafemutablebufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](./unsafemutablebufferpointer/customdebugstringconvertible-implementations.md)
- [MutableCollection Implementations](./unsafemutablebufferpointer/mutablecollection-implementations.md)
- [OperationParameter Implementations](./unsafemutablebufferpointer/operationparameter-implementations.md)
- [Sequence Implementations](./unsafemutablebufferpointer/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/acceleratebuffer.md)
- [AccelerateMutableBuffer](../Accelerate/acceleratemutablebuffer.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BNNSGraph.Builder.OperationParameter](../Accelerate/bnnsgraph/builder/operationparameter.md)
- [BNNSGraph.PointerArgument](../Accelerate/bnnsgraph/pointerargument.md)
- [BidirectionalCollection](./bidirectionalcollection.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [Collection](./collection.md)
- [ContiguousBytes](../Foundation/contiguousbytes.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [Copyable](./copyable.md)
- [CustomDebugStringConvertible](./customdebugstringconvertible.md)
- [Escapable](./escapable.md)
- [MutableCollection](./mutablecollection.md)
- [RandomAccessCollection](./randomaccesscollection.md)
- [Sequence](./sequence.md)

## See Also

### Typed Pointers
- [struct UnsafePointer](./unsafepointer.md)
  A pointer for accessing data of a specific type.
- [struct UnsafeMutablePointer](./unsafemutablepointer.md)
  A pointer for accessing and manipulating data of a specific type.
- [struct UnsafeBufferPointer](./unsafebufferpointer.md)
  A nonowning collection interface to a buffer of elements stored contiguously in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer)*