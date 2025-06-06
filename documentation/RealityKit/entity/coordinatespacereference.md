# Entity.CoordinateSpaceReference

**Framework**: RealityKit  
**Kind**: enum

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

### Operators
- [static func == (Entity.CoordinateSpaceReference, Entity.CoordinateSpaceReference) -> Bool](entity/coordinatespacereference/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Entity.CoordinateSpaceReference.immersiveSpace](entity/coordinatespacereference/immersivespace.md)
  A reference to an opened immersive space.
- [Entity.CoordinateSpaceReference.scene](entity/coordinatespacereference/scene.md)
  A reference to an entity’s parent window scene.
### Instance Properties
- [var hashValue: Int](entity/coordinatespacereference/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](entity/coordinatespacereference/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](entity/coordinatespacereference/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol HasTransform](hastransform.md)
  An interface that enables manipulating the scale, rotation, and translation of an entity.
- [struct Transform](transform.md)
  A component that defines the scale, rotation, and translation of an entity.
- [func transformMatrix(relativeTo: Entity.CoordinateSpaceReference) -> float4x4?](entity/transformmatrix(relativeto:).md)
  Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.
- [Entity.ForwardDirection](entity/forwarddirection.md)
  Defines the forward direction for an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/coordinatespacereference)*