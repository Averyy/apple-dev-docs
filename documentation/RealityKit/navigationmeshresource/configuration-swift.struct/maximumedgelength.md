# maximumEdgeLength

**Framework**: RealityKit  
**Kind**: property

The maximum length of polygon edges in the generated Navigation Mesh, in meters. This value can help modify the resulting Navigation Mesh to have better-looking polygons on maps with long, uninterrupted edges.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var maximumEdgeLength: Double
```

## See Also

- [var maximumSimplificationError: Double](navigationmeshresource/configuration-swift.struct/maximumsimplificationerror.md)
  The maximum deviation that the contours of a generated Navigation Mesh can have from the original mesh, in meters.
- [var maximumVerticesPerPolygon: Int](navigationmeshresource/configuration-swift.struct/maximumverticesperpolygon.md)
  The maximum vertices per polygon used when creating the Navigation Mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/maximumedgelength)*