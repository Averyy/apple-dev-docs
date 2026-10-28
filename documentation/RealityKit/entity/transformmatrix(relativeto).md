# transformMatrix(relativeTo:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func transformMatrix(relativeTo referenceSpace: Entity.CoordinateSpaceReference) -> float4x4?
```

## Return Value

The transform of the entity relative to `referenceSpace`, or `nil` when the given coordinate space is not applicable to the given entity.

## Discussion

This method overloads  [`transformMatrix(relativeTo:)`](../hastransform/transformmatrix%28relativeto%29.md).

## Parameters

- `referenceSpace`: The coordinate space that defines a frame of reference.

## See Also

### Positioning entities in space
- [protocol HasTransform](../hastransform.md)
  An interface that enables manipulating the scale, rotation, and translation of an entity.
- [struct Transform](../transform.md)
  A component that defines the scale, rotation, and translation of an entity.
- [Entity.CoordinateSpaceReference](./coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.
- [Entity.ForwardDirection](./forwarddirection.md)
  Defines the forward direction for an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/transformmatrix(relativeto:))*