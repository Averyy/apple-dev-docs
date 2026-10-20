# componentsPerVector

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of scalar components in each vector.

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
var componentsPerVector: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger componentsPerVector;
```

## See Also

### Inspecting a Geometry Source
- [var data: Data](./data.md)
  The data for the geometry source.
- [var semantic: SCNGeometrySource.Semantic](./semantic-swift.property.md)
  The semantic value (or attribute) the geometry source describes for each vertex.
- [var vectorCount: Int](./vectorcount.md)
  The number of vectors in the data.
- [var usesFloatComponents: Bool](./usesfloatcomponents.md)
  A Boolean value that indicates whether vector components are floating-point values.
- [var bytesPerComponent: Int](./bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](./dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.
- [var dataStride: Int](./datastride.md)
  The number of bytes from a vector to the next one in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/componentspervector)*