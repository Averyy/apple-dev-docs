# Entity.CoordinateSpaceReference

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Defines the coordinate space reference for transform conversion.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum CoordinateSpaceReference
```

#### Overview

Entity uses this option as a reference coordinate space during transform conversion.

Depending on the coordinate space that a caller entity is parented under, and whether there is an immersive space open, some transform conversion case can be inapplicable. Check out each case for more information.

## Topics

### Enumeration Cases
- [Entity.CoordinateSpaceReference.immersiveSpace](./coordinatespacereference/immersivespace.md)
  A reference to an opened immersive space.
- [Entity.CoordinateSpaceReference.scene](./coordinatespacereference/scene.md)
  A reference to an entity’s parent window scene.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Positioning entities in space
- [protocol HasTransform](../hastransform.md)
  An interface that enables manipulating the scale, rotation, and translation of an entity.
- [struct Transform](../transform.md)
  A component that defines the scale, rotation, and translation of an entity.
- [func transformMatrix(relativeTo: Entity.CoordinateSpaceReference) -> float4x4?](./transformmatrix%28relativeto%29.md)
  Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.
- [Entity.ForwardDirection](./forwarddirection.md)
  Defines the forward direction for an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/coordinatespacereference)*