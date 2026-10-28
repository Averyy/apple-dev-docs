# triangleCount

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The number of triangles described by the [`triangleIndices`](./triangleindices-1azi3.md) buffer.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
var triangleCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger triangleCount;
```

## Discussion

Each set of three indices forms a triangle, so the number of indices in the [`triangleIndices`](./triangleindices-1azi3.md) buffer is three times the [`triangleCount`](./trianglecount.md) value.

## See Also

### Accessing Mesh Data
- [var vertices: [simd_float3]](./vertices-43kle.md)
  An array of vertex positions for each point in the plane mesh.
- [var textureCoordinates: [vector_float2]](./texturecoordinates-p801.md)
  An array of texture coordinate values for each point in the plane mesh.
- [var triangleIndices: [Int16]](./triangleindices-64epx.md)
  An array of indices describing the triangle mesh formed by the plane geometry’s vertex data.
- [vertices](./vertices-3kgkm.md)
  A buffer of vertex positions for each point in the plane mesh.
- [vertexCount](./vertexcount.md)
  The number of elements in the [`vertices`](./vertices-3kgkm.md) buffer.
- [textureCoordinates](./texturecoordinates-91pbc.md)
  A buffer of texture coordinate values for each point in the plane mesh.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-91pbc.md) buffer.
- [triangleIndices](./triangleindices-1azi3.md)
  A buffer of indices describing the triangle mesh formed by the plane geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplanegeometry/trianglecount)*