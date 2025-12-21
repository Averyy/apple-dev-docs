# particleSpeedRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s initial speed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var particleSpeedRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the speed of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particleSpeed: CGFloat](skemitternode/particlespeed.md)
  The average initial speed of a new particle, in points per second.
- [var emissionAngle: CGFloat](skemitternode/emissionangle.md)
  The average initial direction of a particle, expressed as an angle in radians.
- [var emissionAngleRange: CGFloat](skemitternode/emissionanglerange.md)
  The range of allowed random values for a particle’s initial direction, expressed as an angle in radians.
- [var xAcceleration: CGFloat](skemitternode/xacceleration.md)
  The acceleration to apply to a particle’s horizontal velocity.
- [var yAcceleration: CGFloat](skemitternode/yacceleration.md)
  The acceleration to apply to a particle’s vertical velocity.
- [var particleZPositionSpeed: CGFloat](skemitternode/particlezpositionspeed.md)
  The speed at which the particle’s depth changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlespeedrange)*