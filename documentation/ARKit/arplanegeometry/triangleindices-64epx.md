# triangleIndices

**Framework**: ARKit  
**Kind**: property

An array of indices describing the triangle mesh formed by the plane geometry’s vertex data.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
@nonobjc
var triangleIndices: [Int16] { get }
```

#### Discussion

Each 16-bit integer value in this array represents an index into the [`vertices`](arplanegeometry/vertices-43kle.md) and [`textureCoordinates`](arplanegeometry/texturecoordinates-p801.md) arrays. Each set of three indices identifies the vertices that form a single triangle in the mesh. You can use array as an index buffer for a triangle mesh in GPU-based rendering or to create 3D model asset files.

Each set of three indices forms a triangle, so the number of indices in the [`triangleIndices`](arplanegeometry/triangleindices-64epx.md) array is three times the [`triangleCount`](arplanegeometry/trianglecount.md) value.

## See Also

- [var vertices: [simd_float3]](arplanegeometry/vertices-43kle.md)
  An array of vertex positions for each point in the plane mesh.
- [var textureCoordinates: [vector_float2]](arplanegeometry/texturecoordinates-p801.md)
  An array of texture coordinate values for each point in the plane mesh.
- [var triangleCount: Int](arplanegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](arplanegeometry/triangleindices-1azi3.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/triangleindices-64epx)*