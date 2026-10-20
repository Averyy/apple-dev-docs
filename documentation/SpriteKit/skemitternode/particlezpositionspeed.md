# particleZPositionSpeed

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The speed at which the particle’s depth changes.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var particleZPositionSpeed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleZPositionSpeed;
```

#### Discussion

The default value is `0.0`.

## See Also

### Controlling Particle Velocity and Acceleration
- [var particleSpeed: CGFloat](./particlespeed.md)
  The average initial speed of a new particle, in points per second.
- [var particleSpeedRange: CGFloat](./particlespeedrange.md)
  The range of allowed random values for a particle’s initial speed.
- [var emissionAngle: CGFloat](./emissionangle.md)
  The average initial direction of a particle, expressed as an angle in radians.
- [var emissionAngleRange: CGFloat](./emissionanglerange.md)
  The range of allowed random values for a particle’s initial direction, expressed as an angle in radians.
- [var xAcceleration: CGFloat](./xacceleration.md)
  The acceleration to apply to a particle’s horizontal velocity.
- [var yAcceleration: CGFloat](./yacceleration.md)
  The acceleration to apply to a particle’s vertical velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlezpositionspeed)*