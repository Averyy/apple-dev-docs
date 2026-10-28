# angle

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The rotation angle, in radians, of the particle about its axis.

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
static let angle: SCNParticleSystem.ParticleProperty
```

```c
extern SCNParticleProperty const SCNParticlePropertyAngle;
```

## Discussion

This property’s value is a floating-point scalar (an [`NSNumber`](../../../Foundation/nsnumber.md) object for particle property controllers, or a single `float` value for particle event or modifier blocks).

The particle system’s [`particleAngle`](../particleangle.md) and [`particleAngleVariation`](../particleanglevariation.md) properties determine the initial rotation for each particle. The [`rotationAxis`](./rotationaxis.md) property defines the particle’s rotation axis.

## See Also

### Type Properties
- [static let angularVelocity: SCNParticleSystem.ParticleProperty](./angularvelocity.md)
  The particle’s angular velocity (or rate of spin), in radians per second.
- [static let bounce: SCNParticleSystem.ParticleProperty](./bounce.md)
  The particle’s restitution coefficient.
- [static let charge: SCNParticleSystem.ParticleProperty](./charge.md)
  The particle’s electric charge, in coulombs.
- [static let color: SCNParticleSystem.ParticleProperty](./color.md)
  The particle’s tint color, as a vector of red, green, blue, and alpha component values.
- [static let contactNormal: SCNParticleSystem.ParticleProperty](./contactnormal.md)
  The normal vector, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let contactPoint: SCNParticleSystem.ParticleProperty](./contactpoint.md)
  The location, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let frame: SCNParticleSystem.ParticleProperty](./frame.md)
  The current frame index of the particle’s image animation.
- [static let frameRate: SCNParticleSystem.ParticleProperty](./framerate.md)
  The rate, in frames per second, of the particle’s image animation.
- [static let friction: SCNParticleSystem.ParticleProperty](./friction.md)
  The particle’s friction coefficient.
- [static let life: SCNParticleSystem.ParticleProperty](./life.md)
  The remaining time in the particle’s life span, in seconds.
- [static let opacity: SCNParticleSystem.ParticleProperty](./opacity.md)
  The particle’s opacity (or alpha value).
- [static let position: SCNParticleSystem.ParticleProperty](./position.md)
  The particle’s position vector in scene coordinate space.
- [static let rotationAxis: SCNParticleSystem.ParticleProperty](./rotationaxis.md)
  The particle’s axis of rotation, expressed as a vector in the particle’s local coordinate space.
- [static let size: SCNParticleSystem.ParticleProperty](./size.md)
  The width and height of the rendered particle image, in units of scene coordinate space.
- [static let velocity: SCNParticleSystem.ParticleProperty](./velocity.md)
  The particle’s velocity vector in units (of scene coordinate space) per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/angle)*