# elements

**Framework**: SceneKit  
**Kind**: property

An array of geometry elements that describe the geometry’s shape.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var elements: [SCNGeometryElement] { get }
```

#### Discussion

Each [`SCNGeometryElement`](scngeometryelement.md) object describes how vertices from the geometry’s sources are combined into polygons to create the geometry’s shape. Visible geometries contain at least one element.

For geometries with multiple elements, you can use the [`materials`](scngeometry/materials.md) property to attach different materials to each element.

## See Also

- [var sources: [SCNGeometrySource]](scngeometry/sources.md)
  An array of geometry sources that provide vertex data for the geometry.
- [var elementCount: Int](scngeometry/elementcount.md)
  The number of geometry elements in the geometry.
- [func element(at: Int) -> SCNGeometryElement](scngeometry/element(at:).md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](scngeometry/sources(for:).md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/elements)*