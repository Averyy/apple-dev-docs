# MeshAnchor.MeshClassification

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The kinds of classification a face of a mesh can have.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: SurfaceClassification)

## Declaration

```swift
enum MeshClassification
```

## Topics

### Getting architecture classifications
- [MeshAnchor.MeshClassification.ceiling](./meshclassification/ceiling.md)
  A ceiling.
- [MeshAnchor.MeshClassification.door](./meshclassification/door.md)
  A door.
- [MeshAnchor.MeshClassification.floor](./meshclassification/floor.md)
  A floor.
- [MeshAnchor.MeshClassification.stairs](./meshclassification/stairs.md)
  A set of stairs.
- [MeshAnchor.MeshClassification.wall](./meshclassification/wall.md)
  A wall.
- [MeshAnchor.MeshClassification.window](./meshclassification/window.md)
  A window.
### Getting furniture classifications
- [MeshAnchor.MeshClassification.bed](./meshclassification/bed.md)
  A bed.
- [MeshAnchor.MeshClassification.cabinet](./meshclassification/cabinet.md)
  A cabinet.
- [MeshAnchor.MeshClassification.homeAppliance](./meshclassification/homeappliance.md)
  A home appliance.
- [MeshAnchor.MeshClassification.seat](./meshclassification/seat.md)
  A seat.
- [MeshAnchor.MeshClassification.table](./meshclassification/table.md)
  A table.
### Getting decoration classifications
- [MeshAnchor.MeshClassification.plant](./meshclassification/plant.md)
  A plant.
- [MeshAnchor.MeshClassification.tv](./meshclassification/tv.md)
  A television.
### Getting unknown classifications
- [MeshAnchor.MeshClassification.none](./meshclassification/none.md)
  An unknown classification.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting mesh information
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a mesh in world space.
- [var geometry: MeshAnchor.Geometry](./geometry-swift.property.md)
  The shape of a mesh anchor.
- [MeshAnchor.Geometry](./geometry-swift.struct.md)
  The shapes that make up a mesh anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/meshanchor/meshclassification)*