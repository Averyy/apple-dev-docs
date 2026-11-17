# ComputeGraphRuntimeComponent

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Manages the live GPU simulation for an entity’s `ComputeGraphComponent_v1`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ComputeGraphRuntimeComponent
```

## Overview

RealityKit creates the ComputeGraphRuntimeComponent automatically on the first frame that a ComputeGraphComponent becomes active. You do not need to add it manually.

## Topics

### Instance Properties
- [var simulation: ComputeGraphSimulation](./computegraphruntimecomponent/simulation.md)
  The underlying compute graph simulation driving this entity.
### Instance Methods
- [func readOutput(ComputeNodeGraph.Port.Address) -> (any MTLBuffer)?](./computegraphruntimecomponent/readoutput%28_%29.md)
  Returns the output buffer for the port at the given address.
- [func readOutputs(ComputeNodeGraph.NodeID) -> [any MTLBuffer]?](./computegraphruntimecomponent/readoutputs%28_%29.md)
  Returns all output buffers for the given output node.

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
- [struct ComputeGraphViewpointComponent](./computegraphviewpointcomponent.md)
  A transient component that provides camera viewpoint information to the particle simulation.
- [class ComputeGraphSharedUniforms](./computegraphshareduniforms.md)
  A transient component that stores typed uniform values shared across all ComputeGraph simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphruntimecomponent)*