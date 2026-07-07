# ComputeNodeGraph.Pipelines

**Framework**: Compute Graph  
**Kind**: struct

Fully-compiled shaders for a compute graph.

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
struct Pipelines
```

#### Overview

You use pipelines to construct [`ComputeGraphSimulation`](computegraphsimulation.md) objects. A pipeline can be used by many simulations at the same time.

## Topics

### Structures
- [ComputeNodeGraph.Pipelines.Options](computenodegraph/pipelines/options-swift.struct.md)
### Initializers
- [init(ComputeNodeGraph) async throws](computenodegraph/pipelines/init(_:)-2h68e.md)
  Assembles and compiles pipelines from the provided graph.
- [init(ComputeNodeGraph) throws](computenodegraph/pipelines/init(_:)-5cutl.md)
  Assembles and compiles pipelines from the provided graph.
- [init(descriptor: ComputeNodeGraph.PipelinesDescriptor) throws](computenodegraph/pipelines/init(descriptor:)-1jzxc.md)
- [init(descriptor: ComputeNodeGraph.PipelinesDescriptor) async throws](computenodegraph/pipelines/init(descriptor:)-2t8g4.md)
### Instance Properties
- [var assembly: ComputeNodeGraph.Assembly](computenodegraph/pipelines/assembly.md)
- [var options: ComputeNodeGraph.Pipelines.Options](computenodegraph/pipelines/options-swift.property.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelines)*