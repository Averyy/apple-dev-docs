# AccelerateBuffer

**Framework**: Accelerate  
**Kind**: protocol

A type that represents an immutable buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
protocol AccelerateBuffer<Element>
```

#### Overview

If you implement your own type that conforms to [`AccelerateBuffer`](acceleratebuffer.md) and uses the default implementation of [`withUnsafeBufferPointer(_:)`](acceleratebuffer/withunsafebufferpointer(_:).md), your type needs to return a nonnil result from [`withContiguousStorageIfAvailable(_:)`](https://developer.apple.com/documentation/Swift/Sequence/withContiguousStorageIfAvailable(_:)-4don7).

## Topics

### Associated Types
- [associatedtype Element](acceleratebuffer/element.md)
  The buffer’s element type.
### Instance Properties
- [var count: Int](acceleratebuffer/count.md)
  The number of elements in the buffer.
### Instance Methods
- [func withUnsafeBufferPointer<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R](acceleratebuffer/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the object’s contiguous storage.

## Relationships

### Inherited By
- [AccelerateMutableBuffer](acceleratemutablebuffer.md)
### Conforming Types
- [vImage.PixelBuffer](vimage/pixelbuffer.md)

## See Also

- [protocol AccelerateMutableBuffer](acceleratemutablebuffer.md)
  A type that represents a mutable buffer.
- [protocol AccelerateMatrixBuffer](acceleratematrixbuffer.md)
- [protocol AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
- [enum AccelerateMatrixOrder](acceleratematrixorder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratebuffer)*