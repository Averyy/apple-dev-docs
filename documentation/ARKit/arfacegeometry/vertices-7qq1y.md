# vertices

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An array of vertex positions for each point in the face mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@nonobjc
var vertices: [simd_float3] { get }
```

## Discussion

Each `float3` value in this array represents the position of a vertex in the mesh, in face coordinates. (See [Tracking Face Position and Orientation](../arfaceanchor.md#Tracking-Face-Position-and-Orientation).)

## See Also

### Accessing Mesh Data
- [var textureCoordinates: [vector_float2]](./texturecoordinates-u42d.md)
  An array of texture coordinate values for each point in the face mesh.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-3tb1o.md) buffer.
- [var triangleIndices: [Int16]](./triangleindices-8isy8.md)
  An array of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/vertices-7qq1y)*