# triangleIndices

**Framework**: ARKit  
**Kind**: property

An array of indices describing the triangle mesh formed by the face geometry’s vertex data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@nonobjc
var triangleIndices: [Int16] { get }
```

#### Discussion

Each 16-bit integer value in this array represents an index into the [`vertices`](arfacegeometry/vertices-fhdb.md) and [`textureCoordinates`](arfacegeometry/texturecoordinates-8ahq1.md) buffers. Each set of three indices identifies the vertices that form a single triangle in the mesh. (That is, this array is appropriate for use as an index buffer for a triangle mesh in GPU-based rendering or creating 3D model asset files.)

Each set of three indices forms a triangle, so the number of indices in the [`triangleIndices`](arfacegeometry/triangleindices-3tb1o.md) buffer is three times the [`triangleCount`](arfacegeometry/trianglecount.md) value.

Face mesh topology is constant across [`ARFaceGeometry`](arfacegeometry.md) instances, so this array always describes the same arrangement of vertices. Only the [`vertices`](arfacegeometry/vertices-7qq1y.md) array changes between face meshes provided by an AR session, indicating the change in vertex positions as ARKit adapts the mesh to the shape and expression of the user’s face.

## See Also

- [var vertices: [simd_float3]](arfacegeometry/vertices-7qq1y.md)
  An array of vertex positions for each point in the face mesh.
- [var textureCoordinates: [vector_float2]](arfacegeometry/texturecoordinates-u42d.md)
  An array of texture coordinate values for each point in the face mesh.
- [var triangleCount: Int](arfacegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](arfacegeometry/triangleindices-3tb1o.md) buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/triangleindices-8isy8)*