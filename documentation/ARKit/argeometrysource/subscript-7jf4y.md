# subscript(_:)

**Framework**: ARKit  
**Kind**: subscript

Provides the number at the subscripted index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
subscript(index: Int32) -> CUnsignedChar { get }
```

#### Discussion

This subscript operates on one-component geometry sources with a [`format`](argeometrysource/format.md) of [`MTLVertexFormat.uchar`](https://developer.apple.com/documentation/Metal/MTLVertexFormat/uchar), such as [`classification`](armeshgeometry/classification.md).

## See Also

- [subscript(Int32) -> (Float, Float, Float)](argeometrysource/subscript(_:)-3v98f.md)
  Provides the source float triplet at the subscripted index.
- [var buffer: any MTLBuffer](argeometrysource/buffer.md)
  A Metal buffer that contains a list of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/subscript(_:)-7jf4y)*