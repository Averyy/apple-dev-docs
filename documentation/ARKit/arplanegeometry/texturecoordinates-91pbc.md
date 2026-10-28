# textureCoordinates

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of texture coordinate values for each point in the plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float2 * textureCoordinates;
```

## Discussion

Each `float2` value in this buffer represents the UV texture coordinates for the vertex at the corresponding index in the [`vertices`](./vertices-3kgkm.md) buffer.

## See Also

### Accessing Mesh Data
- [vertices](./vertices-3kgkm.md)
  A buffer of vertex positions for each point in the plane mesh.
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-3kgkm.md) buffer.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-91pbc.md) buffer.
- [triangleIndices](./triangleindices-1azi3.md)
  A buffer of indices describing the triangle mesh formed by the plane geometry’s vertex data.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-1azi3.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/texturecoordinates-91pbc)*