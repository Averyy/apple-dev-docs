# sources

**Framework**: SceneKit  
**Kind**: property

An array of geometry sources that provide vertex data for the geometry.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var sources: [SCNGeometrySource] { get }
```

#### Discussion

Each [`SCNGeometrySource`](scngeometrysource.md) object describes an attribute of all vertices in the geometry (such as vertex position, surface normal vector, color, or texture mapping coordinates) identified by the source’s [`semantic`](scngeometrysource/semantic-swift.property.md) property. A geometry always has at least one source (for the [`vertex`](scngeometrysource/semantic-swift.struct/vertex.md) semantic), typically has additional sources for use in lighting and shading, and may have other sources for skeletal animation or surface subdivision information.

## See Also

- [var elements: [SCNGeometryElement]](scngeometry/elements.md)
  An array of geometry elements that describe the geometry’s shape.
- [var elementCount: Int](scngeometry/elementcount.md)
  The number of geometry elements in the geometry.
- [func element(at: Int) -> SCNGeometryElement](scngeometry/element(at:).md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](scngeometry/sources(for:).md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/sources)*