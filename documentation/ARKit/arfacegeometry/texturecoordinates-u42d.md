# textureCoordinates

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An array of texture coordinate values for each point in the face mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@nonobjc
var textureCoordinates: [vector_float2] { get }
```

## Discussion

Each `float2` value in this array represents the UV texture coordinates for the vertex at the corresponding index in the [`vertices`](./vertices-fhdb.md) buffer.Face mesh topology is constant across [`ARFaceGeometry`](../arfacegeometry.md) instances, so the values in this array always maps the same vertex indices to the same texture coordinates.

## See Also

### Accessing Mesh Data
- [var vertices: [simd_float3]](./vertices-7qq1y.md)
  An array of vertex positions for each point in the face mesh.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-3tb1o.md) buffer.
- [var triangleIndices: [Int16]](./triangleindices-8isy8.md)
  An array of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/texturecoordinates-u42d)*