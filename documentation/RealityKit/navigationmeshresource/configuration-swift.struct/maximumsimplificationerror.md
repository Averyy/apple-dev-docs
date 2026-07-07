# maximumSimplificationError

**Framework**: RealityKit  
**Kind**: property

The maximum deviation that the contours of a generated Navigation Mesh can have from the original mesh, in meters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maximumSimplificationError: Double
```

## See Also

- [var maximumEdgeLength: Double](navigationmeshresource/configuration-swift.struct/maximumedgelength.md)
  The maximum length of polygon edges in the generated Navigation Mesh, in meters. This value can help modify the resulting Navigation Mesh to have better-looking polygons on maps with long, uninterrupted edges.
- [var maximumVerticesPerPolygon: Int](navigationmeshresource/configuration-swift.struct/maximumverticesperpolygon.md)
  The maximum vertices per polygon used when creating the Navigation Mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/maximumsimplificationerror)*