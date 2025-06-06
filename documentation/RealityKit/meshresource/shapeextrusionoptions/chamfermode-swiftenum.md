# MeshResource.ShapeExtrusionOptions.ChamferMode

**Framework**: RealityKit  
**Kind**: enum

Determines which part of the extrusion to chamfer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ChamferMode
```

## Topics

### Operators
- [static func == (MeshResource.ShapeExtrusionOptions.ChamferMode, MeshResource.ShapeExtrusionOptions.ChamferMode) -> Bool](meshresource/shapeextrusionoptions/chamfermode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MeshResource.ShapeExtrusionOptions.ChamferMode.back](meshresource/shapeextrusionoptions/chamfermode-swift.enum/back.md)
  Only chamfer the back of the extrusion.
- [MeshResource.ShapeExtrusionOptions.ChamferMode.both](meshresource/shapeextrusionoptions/chamfermode-swift.enum/both.md)
  Chamfer both the front and the back of the extrusion.
- [MeshResource.ShapeExtrusionOptions.ChamferMode.front](meshresource/shapeextrusionoptions/chamfermode-swift.enum/front.md)
  Only chamfer the front of the extrusion.
### Instance Properties
- [var hashValue: Int](meshresource/shapeextrusionoptions/chamfermode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](meshresource/shapeextrusionoptions/chamfermode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](meshresource/shapeextrusionoptions/chamfermode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MeshResource.ShapeExtrusionOptions](meshresource/shapeextrusionoptions.md)
  A type that determines the extrusion, chamfering, and material assignment of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.MaterialAssignment](meshresource/shapeextrusionoptions/materialassignment-swift.struct.md)
  A type that determines the material assignments for each part of an extruded shape.
- [MeshResource.ShapeExtrusionOptions.CurveStrokeResolution](meshresource/shapeextrusionoptions/curvestrokeresolution.md)
  Designates the resolution at which a smooth curve is discretized.
- [MeshResource.ShapeExtrusionOptions.ExtrusionMethod](meshresource/shapeextrusionoptions/extrusionmethod-swift.enum.md)
  The options that determine the way in which to extrude a swept shape in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/chamfermode-swift.enum)*