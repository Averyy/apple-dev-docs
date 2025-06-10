# AccelerateMatrixBuffer

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
protocol AccelerateMatrixBuffer<Element>
```

## Topics

### Associated Types
- [associatedtype Element](acceleratematrixbuffer/element.md)
### Instance Properties
- [var accelerateMatrixOrder: AccelerateMatrixOrder](acceleratematrixbuffer/acceleratematrixorder.md)
- [var columnCount: Int](acceleratematrixbuffer/columncount.md)
- [var leadingDimension: Int](acceleratematrixbuffer/leadingdimension.md)
- [var rowCount: Int](acceleratematrixbuffer/rowcount.md)
### Instance Methods
- [func withUnsafeBufferPointer<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R](acceleratematrixbuffer/withunsafebufferpointer(_:).md)

## Relationships

### Inherited By
- [AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
### Conforming Types
- [vImage.PixelBuffer](vimage/pixelbuffer.md)

## See Also

- [protocol AccelerateBuffer](acceleratebuffer.md)
  A type that represents an immutable buffer.
- [protocol AccelerateMutableBuffer](acceleratemutablebuffer.md)
  A type that represents a mutable buffer.
- [protocol AccelerateMutableMatrixBuffer](acceleratemutablematrixbuffer.md)
- [enum AccelerateMatrixOrder](acceleratematrixorder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratematrixbuffer)*