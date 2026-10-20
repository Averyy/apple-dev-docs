# subscript(_:)

**Framework**: ARKit  
**Kind**: subscript  
**Role**: Instance Subscript

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

This subscript operates on one-component geometry sources with a [`format`](./format.md) of [`MTLVertexFormat.uchar`](../../Metal/mtlvertexformat/uchar.md), such as [`classification`](../armeshgeometry/classification.md).

## See Also

### Accessing Geometry
- [subscript(Int32) -> (Float, Float, Float)](./subscript%28_%29-3v98f.md)
  Provides the source float triplet at the subscripted index.
- [var buffer: any MTLBuffer](./buffer.md)
  A Metal buffer that contains a list of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/subscript(_:)-7jf4y)*