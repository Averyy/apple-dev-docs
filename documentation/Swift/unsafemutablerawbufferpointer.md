# UnsafeMutableRawBufferPointer

**Framework**: Swift  
**Kind**: struct

A mutable nonowning collection interface to the bytes in a region of memory.

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
struct UnsafeMutableRawBufferPointer
```

#### Overview

You can use an `UnsafeMutableRawBufferPointer` instance in low-level operations to eliminate uniqueness checks and release mode bounds checks. Bounds checks are always performed in debug mode.

An `UnsafeMutableRawBufferPointer` instance is a view of the raw bytes in a region of memory. Each byte in memory is viewed as a `UInt8` value independent of the type of values held in that memory. Reading from and writing to memory through a raw buffer are untyped operations. Accessing this collection’s bytes does not bind the underlying memory to `UInt8`.

In addition to its collection interface, an `UnsafeMutableRawBufferPointer` instance also supports the following methods provided by `UnsafeMutableRawPointer`, including bounds checks in debug mode:

- `load(fromByteOffset:as:)`
- `loadUnaligned(fromByteOffset:as:)`
- `storeBytes(of:toByteOffset:as:)`
- `copyMemory(from:)`

To access the underlying memory through typed operations, the memory must be bound to a trivial type.

> **Note**: A  can be copied bit for bit with no indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums. Copying memory that contains values of nontrivial types can only be done safely with a typed pointer. Copying bytes directly from nontrivial, in-memory values does not produce valid copies and can only be done by calling a C API, such as `memmove()`.

### Unsafemutablerawbufferpointer Semantics

An `UnsafeMutableRawBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a variable or constant of type `UnsafeMutableRawBufferPointer` does not copy the underlying memory. However, initializing another collection with an `UnsafeMutableRawBufferPointer` instance copies bytes out of the referenced memory and into the new collection.

The following example uses `someBytes`, an `UnsafeMutableRawBufferPointer` instance, to demonstrate the difference between assigning a buffer pointer and using a buffer pointer as the source for another collection’s elements. Here, the assignment to `destBytes` creates a new, nonowning buffer pointer covering the first `n` bytes of the memory that `someBytes` references—nothing is copied:

```swift
var destBytes = someBytes[0..<n]
```

Next, the bytes referenced by `destBytes` are copied into `byteArray`, a new `[UInt8]` array, and then the remainder of `someBytes` is appended to `byteArray`:

```swift
var byteArray: [UInt8] = Array(destBytes)
byteArray += someBytes[n..<someBytes.count]
```

Assigning into a ranged subscript of an `UnsafeMutableRawBufferPointer` instance copies bytes into the memory. The next `n` bytes of the memory that `someBytes` references are copied in this code:

```swift
destBytes[0..<n] = someBytes[n..<(n + n)]
```

## Topics

### Initializers
- [init(UnsafeMutableRawBufferPointer)](unsafemutablerawbufferpointer/init(_:)-5kt34.md)
  Creates a new buffer over the same memory as the given buffer.
- [init<T>(UnsafeMutableBufferPointer<T>)](unsafemutablerawbufferpointer/init(_:)-9dmrh.md)
  Creates a raw buffer over the contiguous bytes in the given typed buffer.
- [init(mutating: UnsafeRawBufferPointer)](unsafemutablerawbufferpointer/init(mutating:).md)
  Creates a new mutable buffer over the same memory as the given buffer.
- [init(rebasing: Slice<UnsafeMutableRawBufferPointer>)](unsafemutablerawbufferpointer/init(rebasing:).md)
  Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.
- [init(start: UnsafeMutableRawPointer?, count: Int)](unsafemutablerawbufferpointer/init(start:count:).md)
  Creates a buffer over the specified number of contiguous bytes starting at the given pointer.
### Instance Properties
- [var baseAddress: UnsafeMutableRawPointer?](unsafemutablerawbufferpointer/baseaddress.md)
  A pointer to the first byte of the buffer.
### Instance Methods
- [func assumingMemoryBound<T>(to: T.Type) -> UnsafeMutableBufferPointer<T>](unsafemutablerawbufferpointer/assumingmemorybound(to:).md)
  Returns a typed buffer to the memory referenced by this buffer, assuming that the memory is already bound to the specified type.
- [func bindMemory<T>(to: T.Type) -> UnsafeMutableBufferPointer<T>](unsafemutablerawbufferpointer/bindmemory(to:).md)
  Binds this buffer’s memory to the specified type and returns a typed buffer of the bound memory.
- [func copyBytes<C>(from: C)](unsafemutablerawbufferpointer/copybytes(from:)-6hg9u.md)
  Copies from a collection of `UInt8` into this buffer’s memory.
- [func copyBytes(from: UnsafeRawBufferPointer)](unsafemutablerawbufferpointer/copybytes(from:)-8y3nw.md)
- [func copyMemory(from: UnsafeRawBufferPointer)](unsafemutablerawbufferpointer/copymemory(from:).md)
  Copies the bytes from the given buffer to this buffer’s memory.
- [func deallocate()](unsafemutablerawbufferpointer/deallocate.md)
  Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [func initializeMemory<S>(as: S.Element.Type, from: S) -> (unwritten: S.Iterator, initialized: UnsafeMutableBufferPointer<S.Element>)](unsafemutablerawbufferpointer/initializememory(as:from:).md)
  Initializes the buffer’s memory with the given elements, binding the initialized memory to the elements’ type.
- [func initializeMemory<C>(as: C.Element.Type, fromContentsOf: C) -> UnsafeMutableBufferPointer<C.Element>](unsafemutablerawbufferpointer/initializememory(as:fromcontentsof:).md)
  Initializes the buffer’s memory with every element of the source, binding the initialized memory to the elements’ type.
- [func initializeMemory<T>(as: T.Type, repeating: T) -> UnsafeMutableBufferPointer<T>](unsafemutablerawbufferpointer/initializememory(as:repeating:).md)
  Initializes the memory referenced by this buffer with the given value, binds the memory to the value’s type, and returns a typed buffer of the initialized memory.
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](unsafemutablerawbufferpointer/load(frombyteoffset:as:).md)
  Returns a new instance of the given type, read from the buffer pointer’s raw memory at the specified byte offset.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](unsafemutablerawbufferpointer/loadunaligned(frombyteoffset:as:)-7883k.md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](unsafemutablerawbufferpointer/loadunaligned(frombyteoffset:as:)-q4sv.md)
- [func moveInitializeMemory<T>(as: T.Type, fromContentsOf: UnsafeMutableBufferPointer<T>) -> UnsafeMutableBufferPointer<T>](unsafemutablerawbufferpointer/moveinitializememory(as:fromcontentsof:)-3gs5r.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func moveInitializeMemory<T>(as: T.Type, fromContentsOf: Slice<UnsafeMutableBufferPointer<T>>) -> UnsafeMutableBufferPointer<T>](unsafemutablerawbufferpointer/moveinitializememory(as:fromcontentsof:)-8gjm9.md)
  Moves every element of an initialized source buffer slice into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type)](unsafemutablerawbufferpointer/storebytes(of:tobyteoffset:as:).md)
  Stores a value’s bytes into the buffer pointer’s raw memory at the specified byte offset.
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeMutableBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](unsafemutablerawbufferpointer/withmemoryrebound(to:_:).md)
  Executes the given closure while temporarily binding the buffer to instances of type `T`.
### Type Methods
- [static func allocate(byteCount: Int, alignment: Int) -> UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer/allocate(bytecount:alignment:).md)
  Allocates uninitialized memory with the specified size and alignment.
- [static func allocate(count: Int) -> UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer/allocate(count:).md)
### Default Implementations
- [AtomicRepresentable Implementations](unsafemutablerawbufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafemutablerawbufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafemutablerawbufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafemutablerawbufferpointer/customdebugstringconvertible-implementations.md)
- [MutableCollection Implementations](unsafemutablerawbufferpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](unsafemutablerawbufferpointer/randomaccesscollection-implementations.md)
- [Sequence Implementations](unsafemutablerawbufferpointer/sequence-implementations.md)

## Relationships

### Conforms To
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
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

- [struct UnsafeRawPointer](unsaferawpointer.md)
  A raw pointer for accessing untyped data.
- [struct UnsafeMutableRawPointer](unsafemutablerawpointer.md)
  A raw pointer for accessing and manipulating untyped data.
- [struct UnsafeRawBufferPointer](unsaferawbufferpointer.md)
  A  nonowning collection interface to the bytes in a region of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/unsafemutablerawbufferpointer)*