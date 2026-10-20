# emissionAngle

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The average initial direction of a particle, expressed as an angle in radians.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var emissionAngle: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat emissionAngle;
```

#### Discussion

The default value is `0.0`.

## See Also

### Controlling Particle Velocity and Acceleration
- [var particleSpeed: CGFloat](./particlespeed.md)
  The average initial speed of a new particle, in points per second.
- [var particleSpeedRange: CGFloat](./particlespeedrange.md)
  The range of allowed random values for a particle’s initial speed.
- [var emissionAngleRange: CGFloat](./emissionanglerange.md)
  The range of allowed random values for a particle’s initial direction, expressed as an angle in radians.
- [var xAcceleration: CGFloat](./xacceleration.md)
  The acceleration to apply to a particle’s horizontal velocity.
- [var yAcceleration: CGFloat](./yacceleration.md)
  The acceleration to apply to a particle’s vertical velocity.
- [var particleZPositionSpeed: CGFloat](./particlezpositionspeed.md)
  The speed at which the particle’s depth changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/emissionangle)*