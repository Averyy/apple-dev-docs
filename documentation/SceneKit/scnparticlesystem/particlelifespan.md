# particleLifeSpan

**Framework**: SceneKit  
**Kind**: property

The duration, in seconds, for which each particle is rendered before being removed from the scene. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var particleLifeSpan: CGFloat { get set }
```

#### Discussion

After each particle is spawned, it appears in the scene for a period of this duration before being removed from the scene. You can randomize the life spans of newly spawned particles with the [`particleLifeSpanVariation`](scnparticlesystem/particlelifespanvariation.md) property.

The default value is `1.0` seconds.

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
- [var particleAngularVelocityVariation: CGFloat](scnparticlesystem/particleangularvelocityvariation.md)
  The range, in degrees per second, of randomized initial angular velocities for particles. Animatable.
- [var particleLifeSpanVariation: CGFloat](scnparticlesystem/particlelifespanvariation.md)
  The range, in seconds, of randomized particle life spans. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlelifespan)*