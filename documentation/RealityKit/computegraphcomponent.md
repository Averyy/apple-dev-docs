# ComputeGraphComponent

**Framework**: RealityKit  
**Kind**: struct

A component that drives a compute graph–based particle simulation on an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ComputeGraphComponent
```

#### Overview

Attach this component to any `Entity` to with a loaded `ComputeGraphResource` and execute it each frame using Metal compute pipelines. The system automatically creates and manages child entities for each graph output, each carrying its own `ModelComponent` and material.

```swift
var component = ComputeGraphComponent(resource: resource)
entity.components.set(component)
```

## Topics

### Structures
- [ComputeGraphComponent.UniformHandle](computegraphcomponent/uniformhandle.md)
### Initializers
- [init()](computegraphcomponent/init.md)
  Creates a `ComputeGraphComponent` with no resource attached.
- [init(resource: ComputeGraphResource)](computegraphcomponent/init(resource:).md)
  Creates a `ComputeGraphComponent` and immediately attaches the given resource.
### Instance Properties
- [var materials: [ComputeNodeGraph.NodeID : any Material]](computegraphcomponent/materials.md)
  Per-output material overrides, keyed by output node identifier.
- [var models: [ComputeNodeGraph.NodeID : ModelComponent]](computegraphcomponent/models.md)
  Per-output model component overrides, keyed by output node identifier.
- [var pipelines: ComputeNodeGraph.Pipelines?](computegraphcomponent/pipelines.md)
  The compiled pipelines used to execute the simulation.
- [var randomSeed: UInt32?](computegraphcomponent/randomseed.md)
  An optional fixed random seed for the simulation.
- [var resource: ComputeGraphResource?](computegraphcomponent/resource.md)
  The compute graph resource that defines the simulation.
- [var simulationRate: ComputeGraphSimulation.SimulationRate](computegraphcomponent/simulationrate.md)
  The rate at which the simulation updates.
- [var state: ComputeGraphComponent.SimulationState](computegraphcomponent/state.md)
  The current playback state of the simulation.
### Instance Methods
- [func fastForward()](computegraphcomponent/fastforward.md)
  Fast-forwards the simulation using the default prewarm behavior.
- [func fastForward(stepCount: Int, stepDeltaTime: Float)](computegraphcomponent/fastforward(stepcount:stepdeltatime:).md)
  Advances the particle simulation by multiple steps in a single operation.
- [func findBufferIndex(port: ComputeNodeGraph.Port.Address) -> Int?](computegraphcomponent/findbufferindex(port:).md)
- [func firstBufferIndex(type: String) -> Int?](computegraphcomponent/firstbufferindex(type:).md)
- [func isOutputEnabled(ComputeNodeGraph.NodeID) -> Bool](computegraphcomponent/isoutputenabled(_:).md)
  Reads the enabled state of an output identified by ID
- [func pause()](computegraphcomponent/pause.md)
  Pauses the simulation, freezing it at its current state.
- [func play()](computegraphcomponent/play.md)
  Resumes the simulation from a paused or stepped state.
- [func replaceUniforms(Data)](computegraphcomponent/replaceuniforms(_:).md)
  Replaces the entire uniform buffer with the given data.
- [func setBuffer((any MTLBuffer)?, bufferOffset: Int, elementCount: Int?, at: Int)](computegraphcomponent/setbuffer(_:bufferoffset:elementcount:at:).md)
  Binds a Metal buffer to a parameter.
- [func setOutputEnabled(ComputeNodeGraph.NodeID, enabled: Bool)](computegraphcomponent/setoutputenabled(_:enabled:).md)
  Sets the enable state of an output identified by ID
- [func setTexture((any MTLTexture)?, at: Int)](computegraphcomponent/settexture(_:at:).md)
  Binds a Metal texture to a parameter at the given index.
- [func setTexture((any MTLTexture)?, port: ComputeNodeGraph.Port.Address) -> Bool](computegraphcomponent/settexture(_:port:).md)
  Binds a Metal texture to a parameter identified by its port address.
- [func setUniformData(RawSpan, for: ComputeGraphComponent.UniformHandle)](computegraphcomponent/setuniformdata(_:for:).md)
  Sets the value of a uniform to raw bytes.
- [func setUniformValue<V>(V, for: ComputeGraphComponent.UniformHandle)](computegraphcomponent/setuniformvalue(_:for:).md)
  Sets the value of a uniform to a `BitwiseCopyable` typed value.
- [func setUniformValue<V>(V, named: String) -> Bool](computegraphcomponent/setuniformvalue(_:named:).md)
  Sets the value of a named uniform to a `BitwiseCopyable` typed value.
- [func spawn(element: ElementSpawnParameters, in: ComputeNodeGraph.NodeID?)](computegraphcomponent/spawn(element:in:).md)
  Spawns a new element in the particle simulation.
- [func spawn(elements: [ElementSpawnParameters], in: ComputeNodeGraph.NodeID?)](computegraphcomponent/spawn(elements:in:).md)
  Spawns elements into the particle simulation.
- [func step()](computegraphcomponent/step.md)
  Advances the simulation by a single frame, then pauses.
- [func uniformHandle(named: String) -> ComputeGraphComponent.UniformHandle?](computegraphcomponent/uniformhandle(named:).md)
  Returns a handle for the named uniform.
### Enumerations
- [ComputeGraphComponent.SimulationState](computegraphcomponent/simulationstate.md)
  The playback state of a compute graph simulation.

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent)*