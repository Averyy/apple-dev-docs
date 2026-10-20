# constrainedAxis

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

### Creating the gesture
- [init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)](./init%28constrainedtoaxis,minimumangledelta%29.md)
  Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle, inputKinds: GestureInputKinds)](./init%28constrainedtoaxis,minimumangledelta,inputkinds%29.md)
  Creates a rotation gesture with a minimum delta for the gesture to start, an axis to constrain measurement of rotation, and the input kinds the gesture should recognize.
- [var minimumAngleDelta: Angle](./minimumangledelta.md)
  The minimum angle delta before the gesture becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotategesture3d/constrainedaxis)*