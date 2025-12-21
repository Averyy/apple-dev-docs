# OutputRawSpan

**Framework**: Swift  
**Kind**: struct

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
  Create an OutputRawSpan with zero capacity
- [init(buffer: UnsafeMutableRawBufferPointer, initializedCount: Int)](outputrawspan/init(buffer:initializedcount:)-1vcj6.md)
  Unsafely create an OutputRawSpan over partly-initialized memory.
- [init(buffer: borrowing Slice<UnsafeMutableRawBufferPointer>, initializedCount: Int)](outputrawspan/init(buffer:initializedcount:)-5sduz.md)
  Unsafely create an OutputRawSpan over partly-initialized memory.
### Instance Properties
- [var byteCount: Int](outputrawspan/bytecount.md)
  The number of initialized bytes in this span.
- [var bytes: RawSpan](outputrawspan/bytes.md)
  Borrow the underlying initialized memory for read-only access.
- [let capacity: Int](outputrawspan/capacity.md)
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
- [func append<T>(T, as: T.Type)](outputrawspan/append(_:as:).md)
  Appends the given value’s bytes to this span’s bytes.
- [func append<T>(repeating: T, count: Int, as: T.Type)](outputrawspan/append(repeating:count:as:).md)
  Appends the given value’s bytes repeatedly to this span’s bytes.
- [func finalize(for: Slice<UnsafeMutableRawBufferPointer>) -> Int](outputrawspan/finalize(for:)-4su35.md)
  Consume the output span (relinquishing its control over the buffer it is addressing), and return the number of initialized bytes in it.
- [func finalize(for: UnsafeMutableRawBufferPointer) -> Int](outputrawspan/finalize(for:)-8oz61.md)
  Consume the output span (relinquishing its control over the buffer it is addressing), and return the number of initialized bytes in it.
- [func removeAll()](outputrawspan/removeall.md)
  Remove all this span’s elements and return its memory to the uninitialized state.
- [func removeLast() -> UInt8](outputrawspan/removelast.md)
  Remove the last byte from this span.
- [func removeLast(Int)](outputrawspan/removelast(_:).md)
  Remove the last N elements, returning the memory they occupy to the uninitialized state.
- [func withUnsafeMutableBytes<E, R>((UnsafeMutableRawBufferPointer, inout Int) throws(E) -> R) throws(E) -> R](outputrawspan/withunsafemutablebytes(_:).md)
  Call the given closure with the unsafe buffer pointer addressed by this OutputRawSpan and a mutable reference to its count of initialized bytes.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan)*