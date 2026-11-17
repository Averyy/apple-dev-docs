# ComputeGraphSharedUniforms

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A transient component that stores typed uniform values shared across all ComputeGraph simulations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class ComputeGraphSharedUniforms
```

## Overview

You add scene-wide uniforms via a `ComputeGraphSharedUniforms` — such as gravity, wind, attractor locations, or a global time offset.

> **Note**: Only one instance of this component should exist in a scene at a time.

## Topics

### Initializers
- [init()](./computegraphshareduniforms/init%28%29.md)
  Creates an empty `ComputeGraphSharedUniforms` component.
### Instance Methods
- [func setUniform<V>(borrowing V)](./computegraphshareduniforms/setuniform%28_%29.md)
  Stores a uniform value, replacing any previously stored value of the same type.
- [func setUniformTransform<V>((V, Entity) -> V)](./computegraphshareduniforms/setuniformtransform%28_%29.md)
  Registers a closure that transforms a uniform value of type `V` on a per-entity basis.
- [func setUniformTransform<V>(type: V.Type, transform: (inout MutableRawSpan, Entity) -> Void)](./computegraphshareduniforms/setuniformtransform%28type,transform%29.md)
  Registers a raw-data transformer closure for a uniform of type `V`.
- [func uniform<V>(V.Type) -> V?](./computegraphshareduniforms/uniform%28_%29.md)
  Returns the stored uniform value for the given type, or `nil` if none has been set.

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
- [struct ComputeGraphViewpointComponent](./computegraphviewpointcomponent.md)
  A transient component that provides camera viewpoint information to the particle simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms)*