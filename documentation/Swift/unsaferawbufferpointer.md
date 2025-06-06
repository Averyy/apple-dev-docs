# UnsafeRawBufferPointer

**Framework**: Swift  
**Kind**: struct

A  nonowning collection interface to the bytes in a region of memory.

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
struct UnsafeRawBufferPointer
```

#### Overview

You can use an `UnsafeRawBufferPointer` instance in low-level operations to eliminate uniqueness checks and release mode bounds checks. Bounds checks are always performed in debug mode.

An `UnsafeRawBufferPointer` instance is a view of the raw bytes in a region of memory. Each byte in memory is viewed as a `UInt8` value independent of the type of values held in that memory. Reading from memory through a raw buffer is an untyped operation.

In addition to its collection interface, an `UnsafeRawBufferPointer` instance also supports the `load(fromByteOffset:as:)` and `loadUnaligned(fromByteOffset:as:)` methods provided by `UnsafeRawPointer`, including bounds checks in debug mode.

To access the underlying memory through typed operations, the memory must be bound to a trivial type.

> **Note**: A  can be copied bit for bit with no indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums. Copying memory that contains values of nontrivial types can only be done safely with a typed pointer. Copying bytes directly from nontrivial, in-memory values does not produce valid copies and can only be done by calling a C API, such as `memmove()`.

A  can be copied bit for bit with no indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums. Copying memory that contains values of nontrivial types can only be done safely with a typed pointer. Copying bytes directly from nontrivial, in-memory values does not produce valid copies and can only be done by calling a C API, such as `memmove()`.

### Unsaferawbufferpointer Semantics

An `UnsafeRawBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a variable or constant of type `UnsafeRawBufferPointer` does not copy the underlying memory. However, initializing another collection with an `UnsafeRawBufferPointer` instance copies bytes out of the referenced memory and into the new collection.

The following example uses `someBytes`, an `UnsafeRawBufferPointer` instance, to demonstrate the difference between assigning a buffer pointer and using a buffer pointer as the source for another collection’s elements. Here, the assignment to `destBytes` creates a new, nonowning buffer pointer covering the first `n` bytes of the memory that `someBytes` references—nothing is copied:

```swift
var destBytes = someBytes[0..<n]
```

Next, the bytes referenced by `destBytes` are copied into `byteArray`, a new `[UInt8]` array, and then the remainder of `someBytes` is appended to `byteArray`:

```swift
var byteArray: [UInt8] = Array(destBytes)
byteArray += someBytes[n..<someBytes.count]
```

## Topics

### Initializers
- [init(UnsafeRawBufferPointer)](unsaferawbufferpointer/init(_:)-24m35.md)
  Creates a new buffer over the same memory as the given buffer.
- [init(UnsafeMutableRawBufferPointer)](unsaferawbufferpointer/init(_:)-5ko6n.md)
  Creates a new buffer over the same memory as the given buffer.
- [init<T>(UnsafeBufferPointer<T>)](unsaferawbufferpointer/init(_:)-9uv4.md)
  Creates a raw buffer over the contiguous bytes in the given typed buffer.
- [init<T>(UnsafeMutableBufferPointer<T>)](unsaferawbufferpointer/init(_:)-rrzw.md)
  Creates a raw buffer over the contiguous bytes in the given typed buffer.
- [init(rebasing: Slice<UnsafeRawBufferPointer>)](unsaferawbufferpointer/init(rebasing:)-9mh4j.md)
  Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.
- [init(rebasing: Slice<UnsafeMutableRawBufferPointer>)](unsaferawbufferpointer/init(rebasing:)-9sxid.md)
  Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.
- [init(start: UnsafeRawPointer?, count: Int)](unsaferawbufferpointer/init(start:count:).md)
  Creates a buffer over the specified number of contiguous bytes starting at the given pointer.
### Instance Properties
- [var baseAddress: UnsafeRawPointer?](unsaferawbufferpointer/baseaddress.md)
  A pointer to the first byte of the buffer.
### Instance Methods
- [func assumingMemoryBound<T>(to: T.Type) -> UnsafeBufferPointer<T>](unsaferawbufferpointer/assumingmemorybound(to:).md)
  Returns a typed buffer to the memory referenced by this buffer, assuming that the memory is already bound to the specified type.
- [func bindMemory<T>(to: T.Type) -> UnsafeBufferPointer<T>](unsaferawbufferpointer/bindmemory(to:).md)
  Binds this buffer’s memory to the specified type and returns a typed buffer of the bound memory.
- [func deallocate()](unsaferawbufferpointer/deallocate.md)
  Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](unsaferawbufferpointer/load(frombyteoffset:as:).md)
  Returns a new instance of the given type, read from the buffer pointer’s raw memory at the specified byte offset.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](unsaferawbufferpointer/loadunaligned(frombyteoffset:as:)-2r9sy.md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](unsaferawbufferpointer/loadunaligned(frombyteoffset:as:)-95fln.md)
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](unsaferawbufferpointer/withmemoryrebound(to:_:).md)
  Executes the given closure while temporarily binding the buffer to instances of type `T`.
### Default Implementations
- [AtomicRepresentable Implementations](unsaferawbufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsaferawbufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsaferawbufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsaferawbufferpointer/customdebugstringconvertible-implementations.md)
- [RandomAccessCollection Implementations](unsaferawbufferpointer/randomaccesscollection-implementations.md)
- [Sequence Implementations](unsaferawbufferpointer/sequence-implementations.md)

## Relationships

### Conforms To
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

- [struct UnsafeRawPointer](unsaferawpointer.md)
  A raw pointer for accessing untyped data.
- [struct UnsafeMutableRawPointer](unsafemutablerawpointer.md)
  A raw pointer for accessing and manipulating untyped data.
- [struct UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
  A mutable nonowning collection interface to the bytes in a region of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer)*