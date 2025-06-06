# init(constrainedToAxis:minimumAngleDelta:)

**Framework**: SwiftUI  
**Kind**: init

Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(constrainedToAxis: RotationAxis3D? = nil, minimumAngleDelta: Angle = .degrees(1))
```

#### Discussion

If the constrained axis is `nil`, the gesture measures unconstrained 3D rotation.

## Parameters

- `constrainedToAxis`: The 3D axis about which rotation is measured.
- `minimumAngleDelta`: The minimum delta required before the   gesture starts. The default value is a one-degree angle.

## See Also

- [var minimumAngleDelta: Angle](rotategesture3d/minimumangledelta.md)
  The minimum angle delta before the gesture becomes active.
- [var constrainedAxis: RotationAxis3D?](rotategesture3d/constrainedaxis.md)
  An axis around which the rotation is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:))*