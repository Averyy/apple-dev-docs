# particleAngularVelocityVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range, in degrees per second, of randomized initial angular velocities for particles. Animatable.

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
var particleAngularVelocityVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleAngularVelocityVariation;
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleAngularVelocity`](./particleangularvelocity.md) property. SceneKit randomly adjusts the initial angular velocity of each particle by up to half the [`particleAngularVelocityVariation`](./particleangularvelocityvariation.md) value. For example, if the [`particleAngularVelocity`](./particleangularvelocity.md) value is `10.0` degrees per second and the [`particleAngularVelocityVariation`](./particleangularvelocityvariation.md) value is `5.0` degrees per second, newly spawned particles spin at random speeds between `7.5` and `12.5` degrees per second.

The default value is `0.0` degrees per second, specifying no randomization.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Motion
- [var particleAngle: CGFloat](./particleangle.md)
  The rotation angle, in degrees, of newly spawned particles. Animatable.
- [var particleAngleVariation: CGFloat](./particleanglevariation.md)
  The range, in degrees of randomized initial particle angles. Animatable.
- [var particleVelocity: CGFloat](./particlevelocity.md)
  The initial speed, in units per second, for newly spawned particles. Animatable.
- [var particleVelocityVariation: CGFloat](./particlevelocityvariation.md)
  The range, in units per second, of randomized initial particle speeds. Animatable.
- [var particleAngularVelocity: CGFloat](./particleangularvelocity.md)
  The initial spin rate, in degrees per second, of newly spawned particles. Animatable.
- [var particleLifeSpan: CGFloat](./particlelifespan.md)
  The duration, in seconds, for which each particle is rendered before being removed from the scene. Animatable.
- [var particleLifeSpanVariation: CGFloat](./particlelifespanvariation.md)
  The range, in seconds, of randomized particle life spans. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleangularvelocityvariation)*