# triangleIndices

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of indices describing the triangle mesh formed by the plane geometry’s vertex data.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```objc
@property (nonatomic, readonly) const int16_t * triangleIndices;
```

## Discussion

Each 16-bit integer value in this buffer represents an index into the [`vertices`](./vertices-3kgkm.md) and [`textureCoordinates`](./texturecoordinates-91pbc.md) buffers. Each set of three indices identifies the vertices that form a single triangle in the mesh. You can use buffer as an index buffer for a triangle mesh in GPU-based rendering or to create 3D model asset files.

Each set of three indices forms a triangle, so the number of indices in the [`triangleIndices`](./triangleindices-1azi3.md) buffer is three times the [`triangleCount`](./trianglecount.md) value.

## See Also

### Accessing Mesh Data
- [vertices](./vertices-3kgkm.md)
  A buffer of vertex positions for each point in the plane mesh.
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-3kgkm.md) buffer.
- [textureCoordinates](./texturecoordinates-91pbc.md)
  A buffer of texture coordinate values for each point in the plane mesh.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-91pbc.md) buffer.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-1azi3.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/triangleindices-1azi3)*