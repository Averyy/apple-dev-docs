# particleAngularVelocityVariation

**Framework**: SceneKit  
**Kind**: property

The range, in degrees per second, of randomized initial angular velocities for particles. Animatable.

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
var particleAngularVelocityVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleAngularVelocity`](scnparticlesystem/particleangularvelocity.md) property. SceneKit randomly adjusts the initial angular velocity of each particle by up to half the [`particleAngularVelocityVariation`](scnparticlesystem/particleangularvelocityvariation.md) value. For example, if the [`particleAngularVelocity`](scnparticlesystem/particleangularvelocity.md) value is `10.0` degrees per second and the [`particleAngularVelocityVariation`](scnparticlesystem/particleangularvelocityvariation.md) value is `5.0` degrees per second, newly spawned particles spin at random speeds between `7.5` and `12.5` degrees per second.

The default value is `0.0` degrees per second, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleAngle: CGFloat](scnparticlesystem/particleangle.md)
  The rotation angle, in degrees, of newly spawned particles. Animatable.
- [var particleAngleVariation: CGFloat](scnparticlesystem/particleanglevariation.md)
  The range, in degrees of randomized initial particle angles. Animatable.
- [var particleVelocity: CGFloat](scnparticlesystem/particlevelocity.md)
  The initial speed, in units per second, for newly spawned particles. Animatable.
- [var particleVelocityVariation: CGFloat](scnparticlesystem/particlevelocityvariation.md)
  The range, in units per second, of randomized initial particle speeds. Animatable.
- [var particleAngularVelocity: CGFloat](scnparticlesystem/particleangularvelocity.md)
  The initial spin rate, in degrees per second, of newly spawned particles. Animatable.
- [var particleLifeSpan: CGFloat](scnparticlesystem/particlelifespan.md)
  The duration, in seconds, for which each particle is rendered before being removed from the scene. Animatable.
- [var particleLifeSpanVariation: CGFloat](scnparticlesystem/particlelifespanvariation.md)
  The range, in seconds, of randomized particle life spans. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleangularvelocityvariation)*