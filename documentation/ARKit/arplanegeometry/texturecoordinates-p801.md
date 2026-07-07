# textureCoordinates

**Framework**: ARKit  
**Kind**: property

An array of texture coordinate values for each point in the plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
@nonobjc
var textureCoordinates: [vector_float2] { get }
```

#### Discussion

Each `float2` value in this array represents the UV texture coordinates for the vertex at the corresponding index in the [`vertices`](arplanegeometry/vertices-43kle.md) array.

## See Also

- [var vertices: [simd_float3]](arplanegeometry/vertices-43kle.md)
  An array of vertex positions for each point in the plane mesh.
- [var triangleCount: Int](arplanegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](arplanegeometry/triangleindices-1azi3.md) buffer.
- [var triangleIndices: [Int16]](arplanegeometry/triangleindices-64epx.md)
  An array of indices describing the triangle mesh formed by the plane geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/texturecoordinates-p801)*