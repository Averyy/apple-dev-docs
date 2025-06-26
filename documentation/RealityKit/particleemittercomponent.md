# ParticleEmitterComponent

**Framework**: RealityKit  
**Kind**: struct

A component that emits particles.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct ParticleEmitterComponent
```

#### Overview

To learn how to use `ParticleEmitterComponent` in your app, see [`Simulating particles in your visionOS app`](simulating-particles-in-your-visionos-app.md).

## Topics

### Structures
- [ParticleEmitterComponent.ParticleEmitter](particleemittercomponent/particleemitter.md)
- [ParticleEmitterComponent.Presets](particleemittercomponent/presets.md)
  Initial configurations that can be set when starting a new simulation.
### Initializers
- [init()](particleemittercomponent/init.md)
### Instance Properties
- [var birthDirection: ParticleEmitterComponent.BirthDirection](particleemittercomponent/birthdirection-swift.property.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.Defaults to normal.
- [var birthLocation: ParticleEmitterComponent.BirthLocation](particleemittercomponent/birthlocation-swift.property.md)
  The possible locations for newly spawned particles, relative to the emitter shape. Defaults to surface.
- [var burstCount: Int](particleemittercomponent/burstcount.md)
  Number of particles to emit in a single burst. Defaults to 100.
- [var burstCountVariation: Int](particleemittercomponent/burstcountvariation.md)
  Defines a plus/minus range from which a value is randomly selected to offset `burstCount`.
- [var emissionDirection: SIMD3<Float>](particleemittercomponent/emissiondirection.md)
  The direction particles are emitted when birthDirection is set to World or Local. Defaults to (0.0, 1.0, 0.0).
- [var emitterShape: ParticleEmitterComponent.EmitterShape](particleemittercomponent/emittershape-swift.property.md)
  The shape of the region of space where the system spawns new particles. Defaults to plane.
- [var emitterShapeSize: SIMD3<Float>](particleemittercomponent/emittershapesize.md)
  The emitter shape size in meters.
- [var fieldSimulationSpace: ParticleEmitterComponent.SimulationSpace](particleemittercomponent/fieldsimulationspace.md)
  Field Simulation Space, either local or global
- [var isEmitting: Bool](particleemittercomponent/isemitting.md)
  Disables/enables particle emission, independent of `simulationState`. Existing particles will not be affected.
- [var mainEmitter: ParticleEmitterComponent.ParticleEmitter](particleemittercomponent/mainemitter.md)
  Particle attributes affecting the main particles of the base simulation.
- [var particlesInheritTransform: Bool](particleemittercomponent/particlesinherittransform.md)
  Determines if the entity’s transformation also affects the particles.
- [var radialAmount: Float](particleemittercomponent/radialamount.md)
  Radial sweep angle for sphere, cylinder, cone, and torus emitter shapes. Defaults to 2 * pi.
- [var simulationState: ParticleEmitterComponent.SimulationState](particleemittercomponent/simulationstate-swift.property.md)
  Controls particle simulation state: playing, paused or stopped. Defaults to `play`.
- [var spawnInheritsParentColor: Bool](particleemittercomponent/spawninheritsparentcolor.md)
  Whether or not the spawnedEmitter’s color should be overriden by the mainEmitter’s color at the time of the spawning.
- [var spawnOccasion: ParticleEmitterComponent.SpawnOccasion](particleemittercomponent/spawnoccasion-swift.property.md)
  Determines when main particles emit spawn particles. Defaults to `onDeath`.
- [var spawnSpreadFactor: Float](particleemittercomponent/spawnspreadfactor.md)
  Amount a spawned particle spreads away from its parent particle, works in conjunction with the spawn particle’s `spreadingAngle`. Defaults to 0.
- [var spawnSpreadFactorVariation: Float](particleemittercomponent/spawnspreadfactorvariation.md)
  Defines a plus/minus range from which a value is randomly selected to offset Spawn Spread Factor.
- [var spawnVelocityFactor: Float](particleemittercomponent/spawnvelocityfactor.md)
  How much of the parent particle’s velocity to inherit. Defaults to 1.
- [var spawnedEmitter: ParticleEmitterComponent.ParticleEmitter?](particleemittercomponent/spawnedemitter.md)
  Attributes affecting secondary particles spawned from the main simulation.
- [var speed: Float](particleemittercomponent/speed.md)
  The initial speed, in meters per second, for newly spawned particles. Defaults to 0.5.
- [var speedVariation: Float](particleemittercomponent/speedvariation.md)
  Defines a plus/minus range (in meters per second) from which a value is randomly selected to offset particle speed.
- [var timing: ParticleEmitterComponent.Timing](particleemittercomponent/timing-swift.property.md)
  Defines the Emitter timing method.
- [var torusInnerRadius: Float](particleemittercomponent/torusinnerradius.md)
  Radius of the torus’ emitter shape tube. Defaults to 0.25.
### Instance Methods
- [func burst()](particleemittercomponent/burst.md)
  Emits burstCount particles on the next update call.
- [func restart()](particleemittercomponent/restart.md)
  Restarts the emission of particles. Requires the component to be re-assigned to the entity to take effect.
### Enumerations
- [ParticleEmitterComponent.BirthDirection](particleemittercomponent/birthdirection-swift.enum.md)
  Options for the initial direction of each emitted particle, used by the birthDirection property.
- [ParticleEmitterComponent.BirthLocation](particleemittercomponent/birthlocation-swift.enum.md)
  Options for the location on the shape of where particles are born, used by the birthLocation property.
- [ParticleEmitterComponent.EmitterShape](particleemittercomponent/emittershape-swift.enum.md)
  Options for the shape of an emitter, used by the emitterShape property.
- [ParticleEmitterComponent.SimulationSpace](particleemittercomponent/simulationspace.md)
  Options for particle simulation space
- [ParticleEmitterComponent.SimulationState](particleemittercomponent/simulationstate-swift.enum.md)
  Options for the particle simulation state, used by the `simulationState` property.
- [ParticleEmitterComponent.SpawnOccasion](particleemittercomponent/spawnoccasion-swift.enum.md)
  Options for when the spawned effect starts, used by the spawnOccasion property.
- [ParticleEmitterComponent.Timing](particleemittercomponent/timing-swift.enum.md)
  Options for specifying the duration of the particle effects, used by the timing property.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [Simulating particles in your visionOS app](simulating-particles-in-your-visionos-app.md)
  Add a range of visual effects to a RealityKit view by attaching a particle emitter component to an entity.
- [ParticleEmitterComponent.ParticleEmitter](particleemittercomponent/particleemitter.md)
- [ParticleEmitterComponent.Presets](particleemittercomponent/presets.md)
  Initial configurations that can be set when starting a new simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent)*