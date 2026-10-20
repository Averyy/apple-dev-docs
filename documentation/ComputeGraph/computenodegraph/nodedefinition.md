# ComputeNodeGraph.NodeDefinition

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

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
struct NodeDefinition
```

## Topics

### Initializers
- [init(name: String, bundle: String?, inputs: [ComputeNodeGraph.PortDefinition], outputs: [ComputeNodeGraph.PortDefinition], kind: ComputeNodeGraph.NodeDefinition.Kind)](./nodedefinition/init%28name,bundle,inputs,outputs,kind%29.md)
- [init(name: String, inputs: [ComputeNodeGraph.PortDefinition], outputs: [ComputeNodeGraph.PortDefinition], kind: ComputeNodeGraph.NodeDefinition.Kind)](./nodedefinition/init%28name,inputs,outputs,kind%29.md)
### Instance Properties
- [var bundle: String?](./nodedefinition/bundle.md)
- [var inputs: [ComputeNodeGraph.PortDefinition]](./nodedefinition/inputs.md)
- [var kind: ComputeNodeGraph.NodeDefinition.Kind](./nodedefinition/kind-swift.property.md)
- [var name: String](./nodedefinition/name.md)
  Name of the NodeDefinition.
- [var outputs: [ComputeNodeGraph.PortDefinition]](./nodedefinition/outputs.md)
### Type Methods
- [static func stage(ComputeNodeGraph.Stage) -> ComputeNodeGraph.NodeDefinition?](./nodedefinition/stage%28_%29.md)
### Enumerations
- [ComputeNodeGraph.NodeDefinition.Kind](./nodedefinition/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Graph definition and assembly
- [struct ComputeNodeGraph](../computenodegraph.md)
- [ComputeNodeGraph.Assembly](./assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](./pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](./pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.Library](./library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](./libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition)*