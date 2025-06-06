# usesFloatComponents

**Framework**: SceneKit  
**Kind**: property

A Boolean value that indicates whether vector components are floating-point values.

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
var usesFloatComponents: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), SceneKit interprets the geometry source’s data as an array of vectors whose components are floating-point values. The type of floating-point value is determined by the [`SCNGeometrySource`](scngeometrysource.md) property: 4 bytes for `float` values or 8 bytes for `double` values.

If [`false`](https://developer.apple.com/documentation/swift/false), SceneKit interprets the geometry source’s data as an array of vectors whose components are integer values. The type of integer value is determined by the [`SCNGeometrySource`](scngeometrysource.md) property; for example, 2 bytes for `unsigned short` values or 4 bytes for `unsigned int` values.

## See Also

- [var data: Data](scngeometrysource/data.md)
  The data for the geometry source.
- [var semantic: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](scngeometrysource/vectorcount.md)
  The number of vectors in the data.
- [var componentsPerVector: Int](scngeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](scngeometrysource/bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](scngeometrysource/dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](scngeometrysource/datastride.md)
  The number of bytes from a vector to the next one in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/usesfloatcomponents)*