# opacity

**Framework**: SceneKit  
**Kind**: property

The particle’s opacity (or alpha value).

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
static let opacity: SCNParticleSystem.ParticleProperty
```

#### Discussion

This property’s value is a floating-point scalar (an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object for particle property controllers, or a single `float` value for particle event or modifier blocks).

This property controls the same alpha value as the [`color`](scnparticlesystem/particleproperty/color.md) property. Use this property when you want to modify particle opacity without modifying color, or when you want to use opacity as the input for a [`SCNParticlePropertyController`](scnparticlepropertycontroller.md) object.

The particle system’s [`particleColor`](scnparticlesystem/particlecolor.md) and [`particleColorVariation`](scnparticlesystem/particlecolorvariation.md) properties determine the initial alpha value for each particle.

## See Also

- [static let angle: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/angle.md)
  The rotation angle, in radians, of the particle about its axis.
- [static let angularVelocity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/angularvelocity.md)
  The particle’s angular velocity (or rate of spin), in radians per second.
- [static let bounce: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/bounce.md)
  The particle’s restitution coefficient.
- [static let charge: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/charge.md)
  The particle’s electric charge, in coulombs.
- [static let color: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/color.md)
  The particle’s tint color, as a vector of red, green, blue, and alpha component values.
- [static let contactNormal: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/contactnormal.md)
  The normal vector, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let contactPoint: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/contactpoint.md)
  The location, in scene coordinate space, of a collision between a particle and a geometry in the scene.
- [static let frame: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/frame.md)
  The current frame index of the particle’s image animation.
- [static let frameRate: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/framerate.md)
  The rate, in frames per second, of the particle’s image animation.
- [static let friction: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/friction.md)
  The particle’s friction coefficient.
- [static let life: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/life.md)
  The remaining time in the particle’s life span, in seconds.
- [static let position: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/position.md)
  The particle’s position vector in scene coordinate space.
- [static let rotationAxis: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/rotationaxis.md)
  The particle’s axis of rotation, expressed as a vector in the particle’s local coordinate space.
- [static let size: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/size.md)
  The width and height of the rendered particle image, in units of scene coordinate space.
- [static let velocity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/velocity.md)
  The particle’s velocity vector in units (of scene coordinate space) per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/opacity)*