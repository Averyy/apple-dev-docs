# AccelerateMutableMatrixBuffer

**Framework**: Accelerate  
**Kind**: protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
protocol AccelerateMutableMatrixBuffer<Element> : AccelerateMatrixBuffer
```

## Topics

### Instance Methods
- [func withUnsafeMutableBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R](acceleratemutablematrixbuffer/withunsafemutablebufferpointer(_:).md)

## Relationships

### Inherits From
- [AccelerateMatrixBuffer](acceleratematrixbuffer.md)
### Conforming Types
- [vImage.PixelBuffer](vimage/pixelbuffer.md)

## See Also

- [protocol AccelerateBuffer](acceleratebuffer.md)
  A type that represents an immutable buffer.
- [protocol AccelerateMutableBuffer](acceleratemutablebuffer.md)
  A type that represents a mutable buffer.
- [protocol AccelerateMatrixBuffer](acceleratematrixbuffer.md)
- [enum AccelerateMatrixOrder](acceleratematrixorder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablematrixbuffer)*