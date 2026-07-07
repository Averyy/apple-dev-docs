# vertices

**Framework**: ARKit  
**Kind**: property

An array of vertex positions for each point in the plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
@nonobjc
var vertices: [simd_float3] { get }
```

#### Discussion

Each `float3` value in this array represents the position of a vertex in the mesh. The owning plane anchor’s [`transform`](aranchor/transform.md) matrix defines the coordinate system for these points.

This array, together with the [`triangleIndices`](arplanegeometry/triangleindices-64epx.md) array, describes a mesh covering the entire surface of the plane. Use this mesh for purposes that involve the filled shape, such as rendering a solid 3D representation of the surface. If, instead, you only need to know the outline of the shape, see the [`boundaryVertices`](arplanegeometry/boundaryvertices-3h98l.md) property.

## See Also

- [var textureCoordinates: [vector_float2]](arplanegeometry/texturecoordinates-p801.md)
  An array of texture coordinate values for each point in the plane mesh.
- [var triangleCount: Int](arplanegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](arplanegeometry/triangleindices-1azi3.md) buffer.
- [var triangleIndices: [Int16]](arplanegeometry/triangleindices-64epx.md)
  An array of indices describing the triangle mesh formed by the plane geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/vertices-43kle)*