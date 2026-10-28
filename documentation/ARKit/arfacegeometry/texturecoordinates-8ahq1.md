# textureCoordinates

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of texture coordinate values for each point in the face mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float2 * textureCoordinates;
```

## Discussion

Each `float2` value in this buffer represents the UV texture coordinates for the vertex at the corresponding index in the [`vertices`](./vertices-fhdb.md) buffer.

The [`textureCoordinateCount`](./texturecoordinatecount.md) property provides the number of elements in the buffer.

Face mesh topology is constant across [`ARFaceGeometry`](../arfacegeometry.md) instances, so the data in this buffer always maps the same vertex indices to the same texture coordinates.

## See Also

### Accessing Mesh Data
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-fhdb.md) buffer.
- [vertices](./vertices-fhdb.md)
  A buffer of vertex positions for each point in the face mesh.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-8ahq1.md) buffer.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-3tb1o.md) buffer.
- [triangleIndices](./triangleindices-3tb1o.md)
  A buffer of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/texturecoordinates-8ahq1)*