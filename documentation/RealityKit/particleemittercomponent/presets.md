# ParticleEmitterComponent.Presets

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Initial configurations that can be set when starting a new simulation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Presets
```

## Topics

### Type Properties
- [static var fireworks: ParticleEmitterComponent](./presets/fireworks.md)
  Particles that emit in regular bursts and spawn secondary particles
- [static var impact: ParticleEmitterComponent](./presets/impact.md)
  Particles that emit in a radial pattern and simulate dust from an object hitting the ground
- [static var magic: ParticleEmitterComponent](./presets/magic.md)
  Particles that twinkle and emit spawn particles
- [static var rain: ParticleEmitterComponent](./presets/rain.md)
  Fast, semi-opaque particles rendered as streaks
- [static var snow: ParticleEmitterComponent](./presets/snow.md)
  Softly falling particles that incorporate motion from a noise pattern
- [static var sparks: ParticleEmitterComponent](./presets/sparks.md)
  Quick and short lived particles that accumulate color to simulate welding sparks

## See Also

### Particle simulation
- [Simulating particles in your visionOS app](../simulating-particles-in-your-visionos-app.md)
  Add a range of visual effects to a RealityKit view by attaching a particle emitter component to an entity.
- [struct ParticleEmitterComponent](../particleemittercomponent.md)
  A component that emits particles.
- [ParticleEmitterComponent.ParticleEmitter](./particleemitter.md)
- [struct ComputeGraphComponent](../computegraphcomponent.md)
  A component that drives a compute graph–based particle simulation on an entity.
- [class ComputeGraphResource](../computegraphresource.md)
  A loaded compute graph resource containing the graph definition, compiled pipelines, and all associated rendering assets.
- [struct ComputeGraphOutputComponent](../computegraphoutputcomponent.md)
  A transient component that identifies the compute graph output associated with an entity.
- [struct ComputeGraphRuntimeComponent](../computegraphruntimecomponent.md)
  Manages the live GPU simulation for an entity’s `ComputeGraphComponent_v1`.
- [struct ComputeGraphViewpointComponent](../computegraphviewpointcomponent.md)
  A transient component that provides camera viewpoint information to the particle simulation.
- [class ComputeGraphSharedUniforms](../computegraphshareduniforms.md)
  A transient component that stores typed uniform values shared across all ComputeGraph simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/presets)*