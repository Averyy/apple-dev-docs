# particleVelocity

**Framework**: SceneKit  
**Kind**: property

The initial speed, in units per second, for newly spawned particles. Animatable.

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
var particleVelocity: CGFloat { get set }
```

#### Discussion

Particles begin moving at this speed in the direction determined by the [`birthDirection`](scnparticlesystem/birthdirection.md) or [`emittingDirection`](scnparticlesystem/emittingdirection.md) property. Their directions and speeds may change thereafter according to the [`acceleration`](scnparticlesystem/acceleration.md) property or physics effects (see the [`isAffectedByGravity`](scnparticlesystem/isaffectedbygravity.md), [`isAffectedByPhysicsFields`](scnparticlesystem/isaffectedbyphysicsfields.md), and [`colliderNodes`](scnparticlesystem/collidernodes.md) properties). You can randomize the speed of newly spawned particles with the [`particleAngularVelocityVariation`](scnparticlesystem/particleangularvelocityvariation.md) property.

Particle speed is measured in units (of the local coordinate space containing the particle system) per second.

The default value is `0.0` units per second, specifying that newly emitted particles are stationary until otherwise influenced.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleAngle: CGFloat](scnparticlesystem/particleangle.md)
  The rotation angle, in degrees, of newly spawned particles. Animatable.
- [var particleAngleVariation: CGFloat](scnparticlesystem/particleanglevariation.md)
  The range, in degrees of randomized initial particle angles. Animatable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlevelocity)*