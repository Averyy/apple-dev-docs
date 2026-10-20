# Entity.ForwardDirection

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Defines the forward direction for an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum ForwardDirection
```

## Topics

### Enumeration Cases
- [Entity.ForwardDirection.negativeZ](./forwarddirection/negativez.md)
- [Entity.ForwardDirection.positiveZ](./forwarddirection/positivez.md)

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
- [Entity.CoordinateSpaceReference](./coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/forwarddirection)*