# subscript(_:)

**Framework**: ARKit  
**Kind**: subscript

Provides the source float triplet at the subscripted index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
@nonobjc
subscript(index: Int32) -> (Float, Float, Float) { get }
```

#### Discussion

This subscript operates on three-component geometry sources with a [`format`](argeometrysource/format.md) of [`MTLVertexFormat.float3`](https://developer.apple.com/documentation/Metal/MTLVertexFormat/float3). This operator returns an (x, y, z) offset relative to its parent anchor’s position that corresponds to the subscripted vertex position in [`vertices`](armeshgeometry/vertices.md) and to the subscripted normal vector in [`normals`](armeshgeometry/normals.md).

## See Also

- [subscript(Int32) -> CUnsignedChar](argeometrysource/subscript(_:)-7jf4y.md)
  Provides the number at the subscripted index.
- [var buffer: any MTLBuffer](argeometrysource/buffer.md)
  A Metal buffer that contains a list of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/subscript(_:)-3v98f)*