# ComputeNodeGraph.Stage

**Framework**: Compute Graph  
**Kind**: struct

An execution context within a compute node graph that groups related nodes into a processing phase.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
struct Stage
```

#### Overview

Stages define the order and purpose of computation passes. In particle systems, stages correspond to phases like emission, initialization, simulation, and output.

## Topics

### Initializers
- [init(String)](computenodegraph/stage/init(_:).md)
### Instance Properties
- [let name: String](computenodegraph/stage/name.md)
  The identifier for this stage
### Instance Methods
- [func canAddNode(with: ComputeNodeGraph.NodeDefinition) -> Bool](computenodegraph/stage/canaddnode(with:).md)
  Whether a node with the given definition can be used in this stage.
### Type Properties
- [static let compute: ComputeNodeGraph.Stage](computenodegraph/stage/compute.md)
  A general-purpose computation stage.
- [static let emission: ComputeNodeGraph.Stage](computenodegraph/stage/emission.md)
  Spawns new particles into the system.
- [static let eventSource: ComputeNodeGraph.Stage](computenodegraph/stage/eventsource.md)
  A stage that receives events from a simulation (e.g. update or terminate), and initializes new particles for another simulation.
- [static let initialize: ComputeNodeGraph.Stage](computenodegraph/stage/initialize.md)
  Sets initial values for newly spawned particles.
- [static let output: ComputeNodeGraph.Stage](computenodegraph/stage/output.md)
  Produces final per-particle results for rendering.
- [static let simulate: ComputeNodeGraph.Stage](computenodegraph/stage/simulate.md)
  Updates particle state each frame (position, velocity, lifetime, etc.).
- [static let texture: ComputeNodeGraph.Stage](computenodegraph/stage/texture.md)
  Generates texture data.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/stage)*