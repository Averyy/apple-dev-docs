# boundaryVertices

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of vertex positions for each point along the plane’s boundary.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float3 * boundaryVertices;
```

## Discussion

Each `float3` value in this buffer represents the position of a vertex along the boundary polygon of the estimated plane. The owning plane anchor’s [`transform`](../aranchor/transform.md) matrix defines the coordinate system for these points.

The [`boundaryVertexCount`](./boundaryvertexcount.md) property provides the number of elements in the buffer.

This buffer defines the boundary polygon of the plane. Use it for purposes that require only that polygon’s definition, such as rendering an outline of the plane’s estimated shape or testing whether a point is inside the bounded region. If, instead, you need the filled shape (for example, to render a solid 3D representation of the surface), see the [`vertices`](./vertices-3kgkm.md) property.

## See Also

### Finding Boundary Points
- [boundaryVertexCount](./boundaryvertexcount.md)
  The number of elements in the [`boundaryVertices`](./boundaryvertices-6nbee.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/boundaryvertices-6nbee)*