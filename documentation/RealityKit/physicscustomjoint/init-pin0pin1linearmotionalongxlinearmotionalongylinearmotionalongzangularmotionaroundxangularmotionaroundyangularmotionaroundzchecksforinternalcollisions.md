# init(pin0:pin1:linearMotionAlongX:linearMotionAlongY:linearMotionAlongZ:angularMotionAroundX:angularMotionAroundY:angularMotionAroundZ:checksForInternalCollisions:)

**Framework**: RealityKit  
**Kind**: init

Creates a new custom joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(pin0: GeometricPin, pin1: GeometricPin, linearMotionAlongX: PhysicsCustomJoint.MotionLimit = .fixed, linearMotionAlongY: PhysicsCustomJoint.MotionLimit = .fixed, linearMotionAlongZ: PhysicsCustomJoint.MotionLimit = .fixed, angularMotionAroundX: PhysicsCustomJoint.MotionLimit = .fixed, angularMotionAroundY: PhysicsCustomJoint.MotionLimit = .fixed, angularMotionAroundZ: PhysicsCustomJoint.MotionLimit = .fixed, checksForInternalCollisions: Bool = false)
```

## Parameters

- `pin0`: The local position and orientation on the first entity.
- `pin1`: The local position and orientation on the second entity.
- `linearMotionAlongX`: The linear motion limits along the x-axis.
- `linearMotionAlongY`: The linear motion limits along the y-axis.
- `linearMotionAlongZ`: The linear motion limits along the z-axis.
- `angularMotionAroundX`: The angular motion limits around the x-axis.
- `angularMotionAroundY`: The angular motion limits around the y-axis.
- `angularMotionAroundZ`: The angular motion limits around the z-axis.
- `checksForInternalCollisions`: A Boolean that indicates whether the joint   checks for collisions between the two   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicscustomjoint/init(pin0:pin1:linearmotionalongx:linearmotionalongy:linearmotionalongz:angularmotionaroundx:angularmotionaroundy:angularmotionaroundz:checksforinternalcollisions:))*