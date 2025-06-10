# AccelerateMutableBuffer

**Framework**: Accelerate  
**Kind**: protocol

A type that represents a mutable buffer.

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
protocol AccelerateMutableBuffer<Element> : AccelerateBuffer
```

#### Overview

If you implement your own type that conforms to [`AccelerateMutableBuffer`](acceleratemutablebuffer.md) and uses the default implementation of [`withUnsafeMutableBufferPointer(_:)`](acceleratemutablebuffer/withunsafemutablebufferpointer(_:).md), your type needs to return a nonnil result from [`withContiguousMutableStorageIfAvailable(_:)`](https://developer.apple.com/documentation/Swift/ContiguousArray/withContiguousMutableStorageIfAvailable(_:)-564v7).

## Topics

### Instance Methods
- [func withUnsafeMutableBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R](acceleratemutablebuffer/withunsafemutablebufferpointer(_:).md)
  Calls the given closure with a pointer to the object’s mutable contiguous storage.
- [func withUnsafePixelBuffer<R>(body: (vImage.PixelBuffer<vImage.Planar16U>) throws -> R) rethrows -> R](acceleratemutablebuffer/withunsafepixelbuffer(body:)-3k58x.md)
- [func withUnsafePixelBuffer<R>(body: (vImage.PixelBuffer<vImage.Planar16F>) throws -> R) rethrows -> R](acceleratemutablebuffer/withunsafepixelbuffer(body:)-5n3lj.md)
- [func withUnsafePixelBuffer<R>(body: (vImage.PixelBuffer<vImage.PlanarF>) throws -> R) rethrows -> R](acceleratemutablebuffer/withunsafepixelbuffer(body:)-9vr8y.md)
- [func withUnsafePixelBuffer<R>(body: (vImage.PixelBuffer<vImage.Planar8>) throws -> R) rethrows -> R](acceleratemutablebuffer/withunsafepixelbuffer(body:)-aa26.md)

## Relationships

### Inherits From
- [AccelerateBuffer](acceleratebuffer.md)
### Conforming Types
- [vImage.PixelBuffer](vimage/pixelbuffer.md)

## See Also

- [protocol AccelerateBuffer](acceleratebuffer.md)
  A type that represents an immutable buffer.
- [protocol AccelerateMatrixBuffer](acceleratematrixbuffer.md)
- [protocol AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
- [enum AccelerateMatrixOrder](acceleratematrixorder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablebuffer)*