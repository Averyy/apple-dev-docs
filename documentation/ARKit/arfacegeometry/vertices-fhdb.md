# vertices

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer of vertex positions for each point in the face mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float3 * vertices;
```

## Discussion

Each `float3` value in this buffer represents the position of a vertex in the mesh, in face coordinates. (See [Tracking Face Position and Orientation](../arfaceanchor.md#Tracking-Face-Position-and-Orientation).)

The [`vertexCount`](./vertexcount.md) property provides the number of elements in the buffer.

## See Also

### Accessing Mesh Data
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-fhdb.md) buffer.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-8ahq1.md) buffer.
- [textureCoordinates](./texturecoordinates-8ahq1.md)
  A buffer of texture coordinate values for each point in the face mesh.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-3tb1o.md) buffer.
- [triangleIndices](./triangleindices-3tb1o.md)
  A buffer of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/vertices-fhdb)*