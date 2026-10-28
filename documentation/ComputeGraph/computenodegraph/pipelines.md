# ComputeNodeGraph.Pipelines

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Fully-compiled shaders for a compute graph.

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
struct Pipelines
```

## Overview

You use pipelines to construct [`ComputeGraphSimulation`](../computegraphsimulation.md) objects. A pipeline can be used by many simulations at the same time.

## Topics

### Structures
- [ComputeNodeGraph.Pipelines.Options](./pipelines/options-swift.struct.md)
### Initializers
- [init(ComputeNodeGraph) async throws](./pipelines/init%28_%29-2h68e.md)
  Assembles and compiles pipelines from the provided graph.
- [init(ComputeNodeGraph) throws](./pipelines/init%28_%29-5cutl.md)
  Assembles and compiles pipelines from the provided graph.
- [init(descriptor: ComputeNodeGraph.PipelinesDescriptor) throws](./pipelines/init%28descriptor%29-1jzxc.md)
- [init(descriptor: ComputeNodeGraph.PipelinesDescriptor) async throws](./pipelines/init%28descriptor%29-2t8g4.md)
### Instance Properties
- [var assembly: ComputeNodeGraph.Assembly](./pipelines/assembly.md)
- [var options: ComputeNodeGraph.Pipelines.Options](./pipelines/options-swift.property.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Graph definition and assembly
- [struct ComputeNodeGraph](../computenodegraph.md)
- [ComputeNodeGraph.Assembly](./assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.PipelinesDescriptor](./pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](./nodedefinition.md)
- [ComputeNodeGraph.Library](./library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](./libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelines)*