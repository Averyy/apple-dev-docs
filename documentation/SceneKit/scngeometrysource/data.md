# data

**Framework**: SceneKit  
**Kind**: property

The data for the geometry source.

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
var data: Data { get }
```

#### Discussion

A geometry source’s data is an array of vectors, each of which represents a particular attribute (or semantic) of a vertex in the geometry. The other properties of the geometry source determine how SceneKit interprets this data. For example, an array of vertex positions may have three 32-bit floating-point components per vector, but an array of texture coordinates may have two 8-bit integer coponents per vector.

## See Also

- [var semantic: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](scngeometrysource/vectorcount.md)
  The number of vectors in the data.
- [var usesFloatComponents: Bool](scngeometrysource/usesfloatcomponents.md)
  A Boolean value that indicates whether vector components are floating-point values.
- [var componentsPerVector: Int](scngeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](scngeometrysource/bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](scngeometrysource/dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](scngeometrysource/datastride.md)
  The number of bytes from a vector to the next one in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/data)*