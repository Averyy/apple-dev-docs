# OutputRawSpan

**Framework**: Swift  
**Kind**: struct

`OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
@frozen
struct OutputRawSpan
```

## Topics

### Initializers
- [init()](outputrawspan/init.md)
  Create an OutputRawSpan with zero capacity.
- [init(buffer: UnsafeMutableRawBufferPointer, initializedCount: Int)](outputrawspan/init(buffer:initializedcount:)-1vcj6.md)
  Unsafely create an OutputRawSpan over partly-initialized memory.
- [init(buffer: borrowing Slice<UnsafeMutableRawBufferPointer>, initializedCount: Int)](outputrawspan/init(buffer:initializedcount:)-5sduz.md)
  Unsafely create an OutputRawSpan over partly-initialized memory.
### Instance Properties
- [var byteCount: Int](outputrawspan/bytecount.md)
  The number of initialized bytes in this span.
- [var byteOffsets: Range<Int>](outputrawspan/byteoffsets.md)
  The indices that are valid for subscripting the span, in ascending order.
- [var bytes: RawSpan](outputrawspan/bytes.md)
  Borrow the underlying initialized memory for read-only access.
- [let capacity: Int](outputrawspan/capacity.md)
  The total number of bytes that this output span can contain.
- [var freeCapacity: Int](outputrawspan/freecapacity.md)
  The number of additional bytes that can be appended to this span.
- [var isEmpty: Bool](outputrawspan/isempty.md)
  A Boolean value indicating whether the span is empty.
- [var isFull: Bool](outputrawspan/isfull.md)
  A Boolean value indicating whether the span is full.
- [var mutableBytes: MutableRawSpan](outputrawspan/mutablebytes.md)
  Exclusively borrow the underlying initialized memory for mutation.
### Instance Methods
- [func append(UInt8)](outputrawspan/append(_:).md)
  Append a single byte to this span.
- [func append<T>(T, as: T.Type)](outputrawspan/append(_:as:)-63w17.md)
  Appends the given value’s bytes to this span’s bytes.
- [func append<T>(T, as: T.Type)](outputrawspan/append(_:as:)-89j87.md)
  Appends the given value’s bytes to this span’s bytes.
- [func append<T>(T, as: T.Type, ByteOrder)](outputrawspan/append(_:as:_:).md)
  Appends the given value’s bytes to this span’s bytes.
- [func append<T>(repeating: T, count: Int, as: T.Type)](outputrawspan/append(repeating:count:as:)-1h8m1.md)
  Appends the given value’s bytes repeatedly to this span’s bytes.
- [func append<T>(repeating: T, count: Int, as: T.Type)](outputrawspan/append(repeating:count:as:)-3z0bf.md)
  Appends the given value’s bytes repeatedly to this span’s bytes.
- [func append<T>(repeating: T, count: Int, as: T.Type, ByteOrder)](outputrawspan/append(repeating:count:as:_:).md)
  Appends the given value’s bytes repeatedly to this span’s bytes.
- [func finalize(for: Slice<UnsafeMutableRawBufferPointer>) -> Int](outputrawspan/finalize(for:)-4su35.md)
  Consume the output span and return the number of initialized bytes.
- [func finalize(for: UnsafeMutableRawBufferPointer) -> Int](outputrawspan/finalize(for:)-8oz61.md)
  Consume the output span and return the number of initialized bytes.
- [func removeAll()](outputrawspan/removeall.md)
  Remove all this span’s bytes and return its memory to the uninitialized state.
- [func removeLast() -> UInt8](outputrawspan/removelast.md)
  Remove the last byte from this span.
- [func removeLast(Int)](outputrawspan/removelast(_:).md)
  Remove the last n bytes from this span, returning the memory they occupy to the uninitialized state.
- [func withUnsafeMutableBytes<E, R>((UnsafeMutableRawBufferPointer, inout Int) throws(E) -> R) throws(E) -> R](outputrawspan/withunsafemutablebytes(_:).md)
  Call the given closure with the unsafe buffer pointer addressed by this OutputRawSpan and a mutable reference to its count of initialized bytes.
### Subscripts
- [subscript(Int) -> UInt8](outputrawspan/subscript(_:).md)
  Accesses the byte at the specified offset in the span.
- [subscript(unchecked _: Int) -> UInt8](outputrawspan/subscript(unchecked:).md)
  Accesses the byte at the specified offset in the span.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
  `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
  `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct MutableRawSpan](mutablerawspan.md)
  `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct SpanIterator](spaniterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan)*