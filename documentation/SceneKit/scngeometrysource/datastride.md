# dataStride

**Framework**: SceneKit  
**Kind**: property

The number of bytes from a vector to the next one in the data.

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
var dataStride: Int { get }
```

#### Discussion

You can use the [`SCNGeometrySource`](scngeometrysource.md) and [`SCNGeometrySource`](scngeometrysource.md) parameters can together to interleave data for multiple geometry sources in the same array, improving rendering performance. See [`SCNGeometrySource`](scngeometrysource.md) for details.

## See Also

- [var data: Data](scngeometrysource/data.md)
  The data for the geometry source.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/datastride)*