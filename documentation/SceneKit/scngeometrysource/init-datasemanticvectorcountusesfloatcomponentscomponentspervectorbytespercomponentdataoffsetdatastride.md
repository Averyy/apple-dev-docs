# init(data:semantic:vectorCount:usesFloatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:)

**Framework**: SceneKit  
**Kind**: init

Creates a geometry source from the specified data and options.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(data: Data, semantic: SCNGeometrySource.Semantic, vectorCount: Int, usesFloatComponents floatComponents: Bool, componentsPerVector: Int, bytesPerComponent: Int, dataOffset offset: Int, dataStride stride: Int)
```

#### Return Value

A new geometry source object.

#### Discussion

A geometry source’s data is an array of vectors, each of which represents a particular attribute (or semantic) of a vertex in the geometry. The other parameters determine how SceneKit interprets this data. For example, an array of vertex positions may have three 32-bit floating-point components per vector, but an array of texture coordinates may have two 8-bit integer coponents per vector. You can use the `offset` and `stride` parameters together to interleave data for multiple geometry sources in the same array, improving rendering performance. See [`SCNGeometrySource`](scngeometrysource.md) for details.

To create a custom [`SCNGeometry`](scngeometry.md) object from the geometry source, use the [`init(sources:elements:)`](scngeometry/init(sources:elements:).md) method.

## Parameters

- `data`: The data for the geometry source.
- `semantic`: The semantic value (or attribute) that the geometry source describes for each vertex. See Geometry Semantic Identifiers for available values.
- `vectorCount`: The number of geometry source vectors.
- `floatComponents`: A Boolean value that indicates whether vector components are floating-point values. Specify   for floating-point values, or   for integer values.
- `componentsPerVector`: The number of scalar components in each vector.
- `bytesPerComponent`: The size, in bytes, of each vector component.
- `offset`: The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- `stride`: The number of bytes from each vector to the next in the data.

## See Also

- [convenience init(vertices: [SCNVector3])](scngeometrysource/init(vertices:).md)
  Creates a geometry source from an array of vertex positions.
- [convenience init(normals: [SCNVector3])](scngeometrysource/init(normals:).md)
  Creates a geometry source from an array of normal vectors.
- [convenience init(textureCoordinates: [CGPoint])](scngeometrysource/init(texturecoordinates:).md)
  Creates a geometry source from an array of texture coordinate points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/init(data:semantic:vectorcount:usesfloatcomponents:componentspervector:bytespercomponent:dataoffset:datastride:))*