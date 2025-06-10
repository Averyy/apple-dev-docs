# edgeCreasesElement

**Framework**: SceneKit  
**Kind**: property

The geometry element identifying which edges of the geometry’s surface should remain sharp after subdivision.

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
var edgeCreasesElement: SCNGeometryElement? { get set }
```

#### Discussion

This geometry element’s [`primitiveType`](scngeometryelement/primitivetype.md) value must be [`SCNGeometryPrimitiveType.line`](scngeometryprimitivetype/line.md). The geometry element’s data is an array of vertex indices, each pair of which defines a line segment identifying an edge to be treated as a crease during subdivision. Use the [`edgeCreasesSource`](scngeometry/edgecreasessource.md) property to specify the smoothness or sharpness of each crease.

## See Also

- [var subdivisionLevel: Int](scngeometry/subdivisionlevel.md)
  The number of subdivisions SceneKit uses to smooth the geometry’s surface at render time.
- [var edgeCreasesSource: SCNGeometrySource?](scngeometry/edgecreasessource.md)
  The geometry source specifying the smoothness or sharpness of edges after surface subdivision.
- [var wantsAdaptiveSubdivision: Bool](scngeometry/wantsadaptivesubdivision.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/edgecreaseselement)*