# semantic

**Framework**: SceneKit  
**Kind**: property

The semantic value (or attribute) the geometry source describes for each vertex.

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
var semantic: SCNGeometrySource.Semantic { get }
```

#### Discussion

A semantic describes an attribute for each vertex, such as position, color, surface normal vector, or texture coordinates.

See [`SCNGeometrySource.Semantic`](scngeometrysource/semantic-swift.struct.md) for available values.

## See Also

- [var data: Data](scngeometrysource/data.md)
  The data for the geometry source.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.property)*