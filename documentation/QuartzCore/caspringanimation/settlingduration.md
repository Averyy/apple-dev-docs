# settlingDuration

**Framework**: Core Animation  
**Kind**: property

The estimated duration required for the spring system to be considered at rest.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var settlingDuration: CFTimeInterval { get }
```

#### Discussion

The duration is evaluated for the current animation parameters and may not the same as the [`duration`](camediatiming/duration.md).

The following code creates a spring animation with a [`duration`](camediatiming/duration.md) of 2 seconds.

```swift
let spring = CASpringAnimation()

spring.keyPath = "position.x"
spring.fromValue = 0
spring.toValue = 640
spring.damping = 5
spring.duration = 2
```

With a damping coefficient of `5`, the settling duration is approximately 2.85 seconds: the animated layer bounces around the target position several times before settling. However, changing the [`damping`](caspringanimation/damping.md) property to `15` reduces the settling duration to just over 1 second: the animated layer quickly comes to a stop as it reaches the target position.

All of the spring animation’s physical attributes: [`damping`](caspringanimation/damping.md), [`initialVelocity`](caspringanimation/initialvelocity.md), [`mass`](caspringanimation/mass.md) and [`stiffness`](caspringanimation/stiffness.md), can affect the settling duration.

## See Also

- [var damping: CGFloat](caspringanimation/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var initialVelocity: CGFloat](caspringanimation/initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var mass: CGFloat](caspringanimation/mass.md)
  The mass of the object attached to the end of the spring.
- [var stiffness: CGFloat](caspringanimation/stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/settlingduration)*