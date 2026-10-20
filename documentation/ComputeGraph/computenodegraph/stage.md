# ComputeNodeGraph.Stage

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

An execution context within a compute node graph that groups related nodes into a processing phase.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct Stage
```

#### Overview

Stages define the order and purpose of computation passes. In particle systems, stages correspond to phases like emission, initialization, simulation, and output.

## Topics

### Initializers
- [init(String)](./stage/init%28_%29.md)
### Instance Properties
- [let name: String](./stage/name.md)
  The identifier for this stage
### Instance Methods
- [func canAddNode(with: ComputeNodeGraph.NodeDefinition) -> Bool](./stage/canaddnode%28with%29.md)
  Whether a node with the given definition can be used in this stage.
### Type Properties
- [static let compute: ComputeNodeGraph.Stage](./stage/compute.md)
  A general-purpose computation stage.
- [static let emission: ComputeNodeGraph.Stage](./stage/emission.md)
  Spawns new particles into the system.
- [static let eventSource: ComputeNodeGraph.Stage](./stage/eventsource.md)
  A stage that receives events from a simulation (e.g. update or terminate), and initializes new particles for another simulation.
- [static let initialize: ComputeNodeGraph.Stage](./stage/initialize.md)
  Sets initial values for newly spawned particles.
- [static let output: ComputeNodeGraph.Stage](./stage/output.md)
  Produces final per-particle results for rendering.
- [static let simulate: ComputeNodeGraph.Stage](./stage/simulate.md)
  Updates particle state each frame (position, velocity, lifetime, etc.).
- [static let texture: ComputeNodeGraph.Stage](./stage/texture.md)
  Generates texture data.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/stage)*