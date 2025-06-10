# rotationAxis

**Framework**: SceneKit  
**Kind**: property

The particle’s axis of rotation, expressed as a vector in the particle’s local coordinate space.

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
static let rotationAxis: SCNParticleSystem.ParticleProperty
```

#### Discussion

This property’s value is a three-component vector (an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object containing an [`SCNVector3`](scnvector3.md) value for particle property controllers, or an array of three `float` values for particle event or modifier blocks).

The particle system’s [`orientationMode`](scnparticlesystem/orientationmode.md) determines the initial rotation axis for each particle. The [`angle`](scnparticlesystem/particleproperty/angle.md) property defines the particle’s rotation about this axis.

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
- [static let opacity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/opacity.md)
  The particle’s opacity (or alpha value).
- [static let position: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/position.md)
  The particle’s position vector in scene coordinate space.
- [static let size: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/size.md)
  The width and height of the rendered particle image, in units of scene coordinate space.
- [static let velocity: SCNParticleSystem.ParticleProperty](scnparticlesystem/particleproperty/velocity.md)
  The particle’s velocity vector in units (of scene coordinate space) per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleproperty/rotationaxis)*