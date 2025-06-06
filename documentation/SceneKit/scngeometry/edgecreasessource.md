# edgeCreasesSource

**Framework**: SceneKit  
**Kind**: property

The geometry source specifying the smoothness or sharpness of edges after surface subdivision.

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
var edgeCreasesSource: SCNGeometrySource? { get set }
```

#### Discussion

This geometry source’s [`semantic`](scngeometrysource/semantic-swift.property.md) value must be [`edgeCrease`](scngeometrysource/semantic-swift.struct/edgecrease.md). Its data is an array of scalar values (that is, the source’s [`componentsPerVector`](scngeometrysource/componentspervector.md) value is `1`). The value at an index in the geometry source determines the smoothness or sharpness of the edge identified by the primitive at the corresponding index in the [`edgeCreasesElement`](scngeometry/edgecreaseselement.md) geometry element: a value of `0.0` specifies a completely smoothed edge, and a value of `10.0` or greater specifies an infinitely sharp edge.

## See Also

- [var subdivisionLevel: Int](scngeometry/subdivisionlevel.md)
  The number of subdivisions SceneKit uses to smooth the geometry’s surface at render time.
- [var edgeCreasesElement: SCNGeometryElement?](scngeometry/edgecreaseselement.md)
  The geometry element identifying which edges of the geometry’s surface should remain sharp after subdivision.
- [var wantsAdaptiveSubdivision: Bool](scngeometry/wantsadaptivesubdivision.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/edgecreasessource)*