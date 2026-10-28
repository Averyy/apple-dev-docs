# particleCharge

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The electric charge, in coulombs, of each particle in the system. Animatable.

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
var particleCharge: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleCharge;
```

## Discussion

A particle’s charge determines its behavior when affected by an electric or magnetic field. Use the [`SCNPhysicsField`](../scnphysicsfield.md) class to add these fields to your scene. Particles with positive or negative charges behave differently when affected by electric or magnetic fields. (Note that while SceneKit uses SI units as the basis for its physics simulation, you need not worry about realism — experiment with different combinations of values to find the behavior that works best for your app or game.) You can randomize the charges of particles in the system with the [`particleChargeVariation`](./particlechargevariation.md) property.

The default value is `0.0` coulombs, making the particle system unaffected by electric or magnetic fields.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Simulating Physics for Particles
- [var isAffectedByGravity: Bool](./isaffectedbygravity.md)
  A Boolean value that determines whether gravity, as defined by the scene’s physics simulation, affects the motion of particles.
- [var isAffectedByPhysicsFields: Bool](./isaffectedbyphysicsfields.md)
  A Boolean value that determines whether physics fields in the scene affect the motion of particles.
- [var colliderNodes: [SCNNode]?](./collidernodes.md)
  The nodes whose geometry the system’s particles can collide with.
- [var particleDiesOnCollision: Bool](./particlediesoncollision.md)
  A Boolean value that determines whether particles are removed from the scene upon colliding with another object.
- [var acceleration: SCNVector3](./acceleration.md)
  The constant acceleration vector, in units per second per second, applied to all particles in the system. Animatable.
- [var dampingFactor: CGFloat](./dampingfactor.md)
  A factor that slows particles relative to their velocity. Animatable.
- [var particleMass: CGFloat](./particlemass.md)
  The mass, in kilograms, of each particle in the system. Animatable.
- [var particleMassVariation: CGFloat](./particlemassvariation.md)
  The range, in kilograms, of randomized particle masses. Animatable.
- [var particleChargeVariation: CGFloat](./particlechargevariation.md)
  The range, in coulombs, of randomized particle charges. Animatable.
- [var particleBounce: CGFloat](./particlebounce.md)
  The restitution coefficient of each particle in the system. Animatable.
- [var particleBounceVariation: CGFloat](./particlebouncevariation.md)
  The range of randomized restitution coefficients for particles. Animatable.
- [var particleFriction: CGFloat](./particlefriction.md)
  The friction coefficient of each particle in the system. Animatable.
- [var particleFrictionVariation: CGFloat](./particlefrictionvariation.md)
  The range of randomized friction coefficients for particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlecharge)*