# MeshResource.ShapeExtrusionOptions.CurveStrokeResolution

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Designates the resolution at which a smooth curve is discretized.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum CurveStrokeResolution
```

## Topics

### Enumeration Cases
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution.uniformSegmentsPerSpan(segmentCount:)](./curvestrokeresolution/uniformsegmentsperspan%28segmentcount%29.md)
  For each span of the curve, generates a uniform number of segments.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### 2D path extrusion for 3D mesh creation
- [MeshResource.ShapeExtrusionOptions](../shapeextrusionoptions.md)
  A type that determines the extrusion, chamfering, and material assignment of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.MaterialAssignment](./materialassignment-swift.struct.md)
  A type that determines the material assignments for each part of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.ChamferMode](./chamfermode-swift.enum.md)
  Determines which part of the extrusion to chamfer.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](./extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/curvestrokeresolution)*