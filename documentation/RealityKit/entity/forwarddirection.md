# Entity.ForwardDirection

**Framework**: RealityKit  
**Kind**: enum

Defines the forward direction for an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum ForwardDirection
```

## Topics

### Operators
- [static func == (Entity.ForwardDirection, Entity.ForwardDirection) -> Bool](entity/forwarddirection/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Entity.ForwardDirection.negativeZ](entity/forwarddirection/negativez.md)
- [Entity.ForwardDirection.positiveZ](entity/forwarddirection/positivez.md)
### Instance Properties
- [var hashValue: Int](entity/forwarddirection/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](entity/forwarddirection/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](entity/forwarddirection/equatable-implementations.md)

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
- [Entity.CoordinateSpaceReference](entity/coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/forwarddirection)*