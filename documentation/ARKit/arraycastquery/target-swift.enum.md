# ARRaycastQuery.Target

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The types of surface you allow a raycast to intersect with.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
enum Target
```

```c
enum ARRaycastTarget : NSInteger;
```

#### Discussion

The available target types are plane, infinite plane, and estimated plane.

## Topics

### Targets
- [ARRaycastQuery.Target.estimatedPlane](./target-swift.enum/estimatedplane.md)
  A raycast target that specifies nonplanar surfaces, or planes about which ARKit can only estimate.
- [ARRaycastQuery.Target.existingPlaneGeometry](./target-swift.enum/existingplanegeometry.md)
  A raycast target that requires a plane to have a definitive size and shape.
- [ARRaycastQuery.Target.existingPlaneInfinite](./target-swift.enum/existingplaneinfinite.md)
  A raycast target that specifies a detected plane, regardless of its size and shape.
### Initializers
- [init?(rawValue: Int)](./target-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the Target
- [var target: ARRaycastQuery.Target](./target-swift.property.md)
  A plane type that allows the raycast to terminate if it’s encountered.
- [var targetAlignment: ARRaycastQuery.TargetAlignment](./targetalignment-swift.property.md)
  The target’s alignment with respect to gravity.
- [ARRaycastQuery.TargetAlignment](./targetalignment-swift.enum.md)
  A specification that indicates a target’s alignment with respect to gravity


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/target-swift.enum)*