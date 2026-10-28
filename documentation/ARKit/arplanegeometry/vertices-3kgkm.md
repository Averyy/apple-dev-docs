# vertices

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of vertex positions for each point in the plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float3 * vertices;
```

## Discussion

Each `float3` value in this buffer represents the position of a vertex in the mesh. The owning plane anchor’s [`transform`](../aranchor/transform.md) matrix defines the coordinate system for these points.

The [`vertexCount`](./vertexcount.md) property provides the number of elements in the buffer.

This buffer, together with the [`triangleIndices`](./triangleindices-1azi3.md) buffer, describes a  mesh covering the entire surface of the plane. Use this mesh for purposes that involve the filled shape, such as rendering a solid 3D representation of the surface. If, instead, you only need to know the outline of the shape, see the [`boundaryVertices`](./boundaryvertices-6nbee.md) property.

## See Also

### Accessing Mesh Data
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-3kgkm.md) buffer.
- [textureCoordinates](./texturecoordinates-91pbc.md)
  A buffer of texture coordinate values for each point in the plane mesh.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-91pbc.md) buffer.
- [triangleIndices](./triangleindices-1azi3.md)
  A buffer of indices describing the triangle mesh formed by the plane geometry’s vertex data.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-1azi3.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/vertices-3kgkm)*