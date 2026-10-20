# MTLPrimitiveType.triangle

**Framework**: Metal  
**Kind**: case  
**Role**: Case

For every separate set of three vertices, rasterize a triangle. If the number of vertices is not a multiple of three, either one or two vertices is ignored.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case triangle
```

```c
MTLPrimitiveTypeTriangle
```

## See Also

### Geometric primitive types
- [MTLPrimitiveType.point](./point.md)
  Rasterize a point at each vertex. The vertex shader needs to provide `[[point_size]]`, or the point size is undefined.
- [MTLPrimitiveType.line](./line.md)
  Rasterize a line between each separate pair of vertices, resulting in a series of unconnected lines. If there are an odd number of vertices, the last vertex is ignored.
- [MTLPrimitiveType.lineStrip](./linestrip.md)
  Rasterize a line between each pair of adjacent vertices, resulting in a series of connected lines (also called a polyline).
- [MTLPrimitiveType.triangleStrip](./trianglestrip.md)
  For every three adjacent vertices, rasterize a triangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitivetype/triangle)*