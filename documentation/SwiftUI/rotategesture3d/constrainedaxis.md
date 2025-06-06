# constrainedAxis

**Framework**: SwiftUI  
**Kind**: property

An axis around which the rotation is constrained.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var constrainedAxis: RotationAxis3D?
```

#### Discussion

If the axis is `nil`, the rotation is unconstrained.

## See Also

- [init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)](rotategesture3d/init(constrainedtoaxis:minimumangledelta:).md)
  Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [var minimumAngleDelta: Angle](rotategesture3d/minimumangledelta.md)
  The minimum angle delta before the gesture becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotategesture3d/constrainedaxis)*