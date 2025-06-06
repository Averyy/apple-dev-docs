# subdivisionLevel

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions SceneKit uses to smooth the geometry’s surface at render time.

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
var subdivisionLevel: Int { get set }
```

#### Discussion

 is a technique for using low-detail geometry to generate a smooth surface for rendering. When you increase the [`subdivisionLevel`](scngeometry/subdivisionlevel.md) value of a geometry, SceneKit automatically splits each face in the rendered surface, creating a more detailed, smoother geometry, as shown in . SceneKit performs this subdivision process at render time, preserving the original geometry data.

![None](https://docs-assets.developer.apple.com/published/198634f31b7c2f613d42c06519779400/media-2929791%402x.png)

Subdividing a surface rounds away any sharp edges and corners in the geometry; however, such details may be important to a model’s design. To preserve edges, use the [`edgeCreasesElement`](scngeometry/edgecreaseselement.md) property to identify edges and the [`edgeCreasesSource`](scngeometry/edgecreasessource.md) property to specify how smooth or sharp they should appear after subdivision. To preserve corners, include a geometry source whose [`semantic`](scngeometrysource/semantic-swift.property.md) value is [`vertexCrease`](scngeometrysource/semantic-swift.struct/vertexcrease.md) when creating the geometry.

The default subdivision level is zero, specifying no subdivision—SceneKit renders the geometry exactly as its vertex data specifies.

## See Also

- [var edgeCreasesElement: SCNGeometryElement?](scngeometry/edgecreaseselement.md)
  The geometry element identifying which edges of the geometry’s surface should remain sharp after subdivision.
- [var edgeCreasesSource: SCNGeometrySource?](scngeometry/edgecreasessource.md)
  The geometry source specifying the smoothness or sharpness of edges after surface subdivision.
- [var wantsAdaptiveSubdivision: Bool](scngeometry/wantsadaptivesubdivision.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/subdivisionlevel)*