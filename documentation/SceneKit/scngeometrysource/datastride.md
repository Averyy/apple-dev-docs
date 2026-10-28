# dataStride

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of bytes from a vector to the next one in the data.

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
var dataStride: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger dataStride;
```

## Discussion

You can use the [`SCNGeometrySource`](../scngeometrysource.md) and [`SCNGeometrySource`](../scngeometrysource.md) parameters can together to interleave data for multiple geometry sources in the same array, improving rendering performance. See [`SCNGeometrySource`](../scngeometrysource.md) for details.

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
- [var componentsPerVector: Int](./componentspervector.md)
  The number of scalar components in each vector.
- [var bytesPerComponent: Int](./bytespercomponent.md)
  The size, in bytes, of each vector component.
- [var dataOffset: Int](./dataoffset.md)
  The offset, in bytes, from the beginning of the data to the first vector component to be used in the geometry source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/datastride)*