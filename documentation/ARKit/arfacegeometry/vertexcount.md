# vertexCount

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The number of elements in the [`vertices`](./vertices-fhdb.md) buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
@property (nonatomic, readonly) NSUInteger vertexCount;
```

## Discussion

Face mesh topology is constant across [`ARFaceGeometry`](../arfacegeometry.md) instances, so the value of this property is the same for all instances.

## See Also

### Accessing Mesh Data
- [vertices](./vertices-fhdb.md)
  A buffer of vertex positions for each point in the face mesh.
- [textureCoordinateCount](./texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./texturecoordinates-8ahq1.md) buffer.
- [textureCoordinates](./texturecoordinates-8ahq1.md)
  A buffer of texture coordinate values for each point in the face mesh.
- [var triangleCount: Int](./trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./triangleindices-3tb1o.md) buffer.
- [triangleIndices](./triangleindices-3tb1o.md)
  A buffer of indices describing the triangle mesh formed by the face geometry’s vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry/vertexcount)*