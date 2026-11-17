# ComputeGraphViewpointComponent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A transient component that provides camera viewpoint information to the particle simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ComputeGraphViewpointComponent
```

## Overview

Attach this component to an entity to supply the simulation with an observer’s position and direction. The simulation uses these values for view-dependent effects such as billboard orientation or camera-facing particles.

Both properties are optional. When `nil`, the simulation falls back to its default viewpoint behavior.

## Topics

### Initializers
- [init()](./computegraphviewpointcomponent/init%28%29.md)
### Instance Properties
- [var viewDirection: SIMD3<Float>?](./computegraphviewpointcomponent/viewdirection.md)
  The direction the observer is facing, in world space.
- [var viewPosition: SIMD3<Float>?](./computegraphviewpointcomponent/viewposition.md)
  The position of the observer, in world space.

## Relationships

### Conforms To
- [Component](./component.md)
- [TransientComponent](./transientcomponent.md)

## See Also

### Particle simulation
- [Simulating particles in your visionOS app](./simulating-particles-in-your-visionos-app.md)
  Add a range of visual effects to a RealityKit view by attaching a particle emitter component to an entity.
- [struct ParticleEmitterComponent](./particleemittercomponent.md)
  A component that emits particles.
- [ParticleEmitterComponent.ParticleEmitter](./particleemittercomponent/particleemitter.md)
- [ParticleEmitterComponent.Presets](./particleemittercomponent/presets.md)
  Initial configurations that can be set when starting a new simulation.
- [struct ComputeGraphComponent](./computegraphcomponent.md)
  A component that drives a compute graph–based particle simulation on an entity.
- [class ComputeGraphResource](./computegraphresource.md)
  A loaded compute graph resource containing the graph definition, compiled pipelines, and all associated rendering assets.
- [struct ComputeGraphOutputComponent](./computegraphoutputcomponent.md)
  A transient component that identifies the compute graph output associated with an entity.
- [struct ComputeGraphRuntimeComponent](./computegraphruntimecomponent.md)
  Manages the live GPU simulation for an entity’s `ComputeGraphComponent_v1`.
- [class ComputeGraphSharedUniforms](./computegraphshareduniforms.md)
  A transient component that stores typed uniform values shared across all ComputeGraph simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphviewpointcomponent)*