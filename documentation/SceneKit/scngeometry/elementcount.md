# elementCount

**Framework**: SceneKit  
**Kind**: property

The number of geometry elements in the geometry.

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
var elementCount: Int { get }
```

#### Discussion

Each [`SCNGeometryElement`](scngeometryelement.md) object describes how vertices from the geometry’s sources are combined into polygons to create the geometry’s shape. Visible geometries contain at least one element.

For geometries with multiple elements, you can use the [`materials`](scngeometry/materials.md) property to attach different materials to each element.

## See Also

- [var elements: [SCNGeometryElement]](scngeometry/elements.md)
  An array of geometry elements that describe the geometry’s shape.
- [var sources: [SCNGeometrySource]](scngeometry/sources.md)
  An array of geometry sources that provide vertex data for the geometry.
- [func element(at: Int) -> SCNGeometryElement](scngeometry/element(at:).md)
  Returns the geometry element at a specified index.
- [func sources(for: SCNGeometrySource.Semantic) -> [SCNGeometrySource]](scngeometry/sources(for:).md)
  Returns the geometry sources for a specified semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/elementcount)*