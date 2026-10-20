# sources

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An array of geometry sources that provide vertex data for the geometry.

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
var sources: [SCNGeometrySource] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SCNGeometrySource *> * geometrySources;
```

#### Discussion

Each [`SCNGeometrySource`](../scngeometrysource.md) object describes an attribute of all vertices in the geometry (such as vertex position, surface normal vector, color, or texture mapping coordinates) identified by the source’s [`semantic`](../scngeometrysource/semantic-swift.property.md) property. A geometry always has at least one source (for the [`vertex`](../scngeometrysource/semantic-swift.struct/vertex.md) semantic), typically has additional sources for use in lighting and shading, and may have other sources for skeletal animation or surface subdivision information.

## See Also

### Managing Geometry Data
- [var elements: [SCNGeometryElement]](./elements.md)
  An array of geometry elements that describe the geometry’s shape.
- [var elementCount: Int](./elementcount.md)
  The number of geometry elements in the geometry.
- [func element(at: Int) -> SCNGeometryElement](./element%28at%29.md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](./sources%28for%29.md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/sources)*