# MeshResource.ShapeExtrusionOptions

**Framework**: RealityKit  
**Kind**: struct

A type that determines the extrusion, chamfering, and material assignment of an extruded shape.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ShapeExtrusionOptions
```

## Topics

### Structures
- [MeshResource.ShapeExtrusionOptions.MaterialAssignment](meshresource/shapeextrusionoptions/materialassignment-swift.struct.md)
  A type that determines the material assignments for each part of an extruded shape.
### Initializers
- [init()](meshresource/shapeextrusionoptions/init.md)
  Creates the shape extrusion options with default values.
### Instance Properties
- [var boundaryResolution: MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](meshresource/shapeextrusionoptions/boundaryresolution.md)
  Resolution of the shape.
- [var chamferMode: MeshResource.ShapeExtrusionOptions.ChamferMode](meshresource/shapeextrusionoptions/chamfermode-swift.property.md)
  Determines if the front, back or both sides should be chamfered.
- [var chamferProfile: Path?](meshresource/shapeextrusionoptions/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: Float](meshresource/shapeextrusionoptions/chamferradius.md)
  The width or depth, in meters, of each chamfered edge.
- [var chamferResolution: MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](meshresource/shapeextrusionoptions/chamferresolution.md)
  Resolution of the chamfer curve.
- [var extrusionMethod: MeshResource.ShapeExtrusionOptions.ExtrusionMethod](meshresource/shapeextrusionoptions/extrusionmethod-swift.property.md)
  Specifies the extrusion type applied to the swept shape in 3D space.
- [var materialAssignment: MeshResource.ShapeExtrusionOptions.MaterialAssignment](meshresource/shapeextrusionoptions/materialassignment-swift.property.md)
  Determines the material assignments for each part of an extruded shape.
### Enumerations
- [MeshResource.ShapeExtrusionOptions.ChamferMode](meshresource/shapeextrusionoptions/chamfermode-swift.enum.md)
  Determines which part of the extrusion to chamfer.
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](meshresource/shapeextrusionoptions/curvestrokeresolution.md)
  Designates the resolution at which a smooth curve is discretized.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](meshresource/shapeextrusionoptions/extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MeshResource.ShapeExtrusionOptions.MaterialAssignment](meshresource/shapeextrusionoptions/materialassignment-swift.struct.md)
  A type that determines the material assignments for each part of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.ChamferMode](meshresource/shapeextrusionoptions/chamfermode-swift.enum.md)
  Determines which part of the extrusion to chamfer.
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](meshresource/shapeextrusionoptions/curvestrokeresolution.md)
  Designates the resolution at which a smooth curve is discretized.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](meshresource/shapeextrusionoptions/extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions)*