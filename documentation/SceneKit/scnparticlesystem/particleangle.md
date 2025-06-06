# particleAngle

**Framework**: SceneKit  
**Kind**: property

The rotation angle, in degrees, of newly spawned particles. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var particleAngle: CGFloat { get set }
```

#### Discussion

A particle’s angle (or orientation) is independent from its direction of motion. For example, a smoke effect may use a small image of a cloud for each particle, which stays at the same angle as the smoke rises, but a snow effect may use an image that flips and rotates as each snowflake falls. The [`orientationMode`](scnparticlesystem/orientationmode.md) property determines whether and how particles are allowed to rotate, and the [`particleAngle`](scnparticlesystem/particleangle.md) and [`particleAngularVelocity`](scnparticlesystem/particleangularvelocity.md) properties determine rotation angles and rates. You can randomize the rotations of newly spawned particles with the [`particleAngleVariation`](scnparticlesystem/particleanglevariation.md) property.

The default value is `0.0` degrees, specifying no rotation.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleAngleVariation: CGFloat](scnparticlesystem/particleanglevariation.md)
  The range, in degrees of randomized initial particle angles. Animatable.
- [var particleVelocity: CGFloat](scnparticlesystem/particlevelocity.md)
  The initial speed, in units per second, for newly spawned particles. Animatable.
- [var particleVelocityVariation: CGFloat](scnparticlesystem/particlevelocityvariation.md)
  The range, in units per second, of randomized initial particle speeds. Animatable.
- [var particleAngularVelocity: CGFloat](scnparticlesystem/particleangularvelocity.md)
  The initial spin rate, in degrees per second, of newly spawned particles. Animatable.
- [var particleAngularVelocityVariation: CGFloat](scnparticlesystem/particleangularvelocityvariation.md)
  The range, in degrees per second, of randomized initial angular velocities for particles. Animatable.
- [var particleLifeSpan: CGFloat](scnparticlesystem/particlelifespan.md)
  The duration, in seconds, for which each particle is rendered before being removed from the scene. Animatable.
- [var particleLifeSpanVariation: CGFloat](scnparticlesystem/particlelifespanvariation.md)
  The range, in seconds, of randomized particle life spans. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleangle)*