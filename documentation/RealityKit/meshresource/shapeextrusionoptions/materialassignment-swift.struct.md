# MeshResource.ShapeExtrusionOptions.MaterialAssignment

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A type that determines the material assignments for each part of an extruded shape.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct MaterialAssignment
```

## Topics

### Initializers
- [init(assignAll: UInt32)](./materialassignment-swift.struct/init%28assignall%29.md)
  Creates a material assignment structure that assigns the same material to all faces.
- [init(front: UInt32, back: UInt32, extrusion: UInt32, frontChamfer: UInt32, backChamfer: UInt32)](./materialassignment-swift.struct/init%28front,back,extrusion,frontchamfer,backchamfer%29.md)
  Creates a material assignment structure with options for each side of an extruded shape.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### 2D path extrusion for 3D mesh creation
- [MeshResource.ShapeExtrusionOptions](../shapeextrusionoptions.md)
  A type that determines the extrusion, chamfering, and material assignment of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.ChamferMode](./chamfermode-swift.enum.md)
  Determines which part of the extrusion to chamfer.
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](./curvestrokeresolution.md)
  Designates the resolution at which a smooth curve is discretized.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](./extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/materialassignment-swift.struct)*