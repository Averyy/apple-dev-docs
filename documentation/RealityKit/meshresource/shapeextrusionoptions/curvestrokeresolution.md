# MeshResource.ShapeExtrusionOptions.CurveStrokeResolution

**Framework**: RealityKit  
**Kind**: enum

Designates the resolution at which a smooth curve is discretized.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum CurveStrokeResolution
```

## Topics

### Enumeration Cases
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution.uniformSegmentsPerSpan(segmentCount:)](meshresource/shapeextrusionoptions/curvestrokeresolution/uniformsegmentsperspan(segmentcount:).md)
  For each span of the curve, generates a uniform number of segments.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [MeshResource.ShapeExtrusionOptions](meshresource/shapeextrusionoptions.md)
  A type that determines the extrusion, chamfering, and material assignment of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.MaterialAssignment](meshresource/shapeextrusionoptions/materialassignment-swift.struct.md)
  A type that determines the material assignments for each part of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.ChamferMode](meshresource/shapeextrusionoptions/chamfermode-swift.enum.md)
  Determines which part of the extrusion to chamfer.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](meshresource/shapeextrusionoptions/extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/curvestrokeresolution)*