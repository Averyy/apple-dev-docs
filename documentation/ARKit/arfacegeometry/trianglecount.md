# triangleCount

**Framework**: ARKit  
**Kind**: property

The number of triangles described by the [`triangleIndices`](arfacegeometry/triangleindices-3tb1o.md) buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var triangleCount: Int { get }
```

#### Discussion

Each set of three indices forms a triangle, so the number of indices in the [`triangleIndices`](arfacegeometry/triangleindices-3tb1o.md) buffer is three times the [`triangleCount`](arfacegeometry/trianglecount.md) value.

Face mesh topology is constant across [`ARFaceGeometry`](arfacegeometry.md) instances, so the value of this property is the same for all instances.

## See Also

- [var vertices: [simd_float3]](arfacegeometry/vertices-7qq1y.md)
  An array of vertex positions for each point in the face mesh.
- [var textureCoordinates: [vector_float2]](arfacegeometry/texturecoordinates-u42d.md)
  An array of texture coordinate values for each point in the face mesh.
- [var triangleIndices: [Int16]](arfacegeometry/triangleindices-8isy8.md)
  An array of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/trianglecount)*