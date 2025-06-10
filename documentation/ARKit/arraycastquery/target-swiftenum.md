# ARRaycastQuery.Target

**Framework**: ARKit  
**Kind**: enum

The types of surface you allow a raycast to intersect with.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Target
```

#### Discussion

The available target types are plane, infinite plane, and estimated plane.

## Topics

### Targets
- [ARRaycastQuery.Target.estimatedPlane](arraycastquery/target-swift.enum/estimatedplane.md)
  A raycast target that specifies nonplanar surfaces, or planes about which ARKit can only estimate.
- [ARRaycastQuery.Target.existingPlaneGeometry](arraycastquery/target-swift.enum/existingplanegeometry.md)
  A raycast target that requires a plane to have a definitive size and shape.
- [ARRaycastQuery.Target.existingPlaneInfinite](arraycastquery/target-swift.enum/existingplaneinfinite.md)
  A raycast target that specifies a detected plane, regardless of its size and shape.
### Initializers
- [init?(rawValue: Int)](arraycastquery/target-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var target: ARRaycastQuery.Target](arraycastquery/target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.
- [ARRaycastQuery.TargetAlignment](arraycastquery/targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/target-swift.enum)*