# data

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The data for the geometry source.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var data: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * data;
```

#### Discussion

A geometry source’s data is an array of vectors, each of which represents a particular attribute (or semantic) of a vertex in the geometry. The other properties of the geometry source determine how SceneKit interprets this data. For example, an array of vertex positions may have three 32-bit floating-point components per vector, but an array of texture coordinates may have two 8-bit integer coponents per vector.

## See Also

### Inspecting a Geometry Source
- [var semantic: SCNGeometrySource.Semantic](./semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](./vectorcount.md)
  The number of vectors in the data.
- [var usesFloatComponents: Bool](./usesfloatcomponents.md)
  A Boolean value that indicates whether vector components are floating-point values.
- [var componentsPerVector: Int](./componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](./bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](./dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](./datastride.md)
  The number of bytes from a vector to the next one in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/data)*