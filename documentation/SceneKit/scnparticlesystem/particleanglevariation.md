# particleAngleVariation

**Framework**: SceneKit  
**Kind**: property

The range, in degrees of randomized initial particle angles. Animatable.

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
var particleAngleVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleAngle`](scnparticlesystem/particleangle.md) property. SceneKit randomly adjusts the initial angle of each particle by up to half the [`particleAngleVariation`](scnparticlesystem/particleanglevariation.md) value. For example, if the [`particleAngle`](scnparticlesystem/particleangle.md) value is `90.0` degrees and the [`particleAngleVariation`](scnparticlesystem/particleanglevariation.md) value is `30.0` degrees, newly spawned particles are randomly rotated to an angle between 75° and 105°.

The default value is `0.0` degrees, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleAngle: CGFloat](scnparticlesystem/particleangle.md)
  The rotation angle, in degrees, of newly spawned particles. Animatable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleanglevariation)*