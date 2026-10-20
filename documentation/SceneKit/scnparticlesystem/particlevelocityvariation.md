# particleVelocityVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range, in units per second, of randomized initial particle speeds. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var particleVelocityVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleVelocityVariation;
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleVelocity`](./particlevelocity.md) property. SceneKit randomly adjusts the initial speed of each particle by up to half the [`particleVelocityVariation`](./particlevelocityvariation.md) value. For example, if the [`particleVelocity`](./particlevelocity.md) value is `10.0` units per second and the [`particleVelocityVariation`](./particlevelocityvariation.md) value is `5.0` units per second, newly spawned particles have random velocities between `7.5` and `12.5` units per second.

The default value is `0.0` units per second, specifying no randomization.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Motion
- [var particleAngle: CGFloat](./particleangle.md)
  The rotation angle, in degrees, of newly spawned particles. Animatable.
- [var particleAngleVariation: CGFloat](./particleanglevariation.md)
  The range, in degrees of randomized initial particle angles. Animatable.
- [var particleVelocity: CGFloat](./particlevelocity.md)
  The initial speed, in units per second, for newly spawned particles. Animatable.
- [var particleAngularVelocity: CGFloat](./particleangularvelocity.md)
  The initial spin rate, in degrees per second, of newly spawned particles. Animatable.
- [var particleAngularVelocityVariation: CGFloat](./particleangularvelocityvariation.md)
  The range, in degrees per second, of randomized initial angular velocities for particles. Animatable.
- [var particleLifeSpan: CGFloat](./particlelifespan.md)
  The duration, in seconds, for which each particle is rendered before being removed from the scene. Animatable.
- [var particleLifeSpanVariation: CGFloat](./particlelifespanvariation.md)
  The range, in seconds, of randomized particle life spans. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlevelocityvariation)*