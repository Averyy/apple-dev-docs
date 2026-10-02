# ComputeNodeGraph.NodeDefinition

**Framework**: Compute Graph  
**Kind**: struct

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
struct NodeDefinition
```

## Topics

### Initializers
- [init(name: String, bundle: String?, inputs: [ComputeNodeGraph.PortDefinition], outputs: [ComputeNodeGraph.PortDefinition], kind: ComputeNodeGraph.NodeDefinition.Kind)](computenodegraph/nodedefinition/init(name:bundle:inputs:outputs:kind:).md)
- [init(name: String, inputs: [ComputeNodeGraph.PortDefinition], outputs: [ComputeNodeGraph.PortDefinition], kind: ComputeNodeGraph.NodeDefinition.Kind)](computenodegraph/nodedefinition/init(name:inputs:outputs:kind:).md)
### Instance Properties
- [var bundle: String?](computenodegraph/nodedefinition/bundle.md)
- [var inputs: [ComputeNodeGraph.PortDefinition]](computenodegraph/nodedefinition/inputs.md)
- [var kind: ComputeNodeGraph.NodeDefinition.Kind](computenodegraph/nodedefinition/kind-swift.property.md)
- [var name: String](computenodegraph/nodedefinition/name.md)
  Name of the NodeDefinition.
- [var outputs: [ComputeNodeGraph.PortDefinition]](computenodegraph/nodedefinition/outputs.md)
### Type Methods
- [static func stage(ComputeNodeGraph.Stage) -> ComputeNodeGraph.NodeDefinition?](computenodegraph/nodedefinition/stage(_:).md)
### Enumerations
- [ComputeNodeGraph.NodeDefinition.Kind](computenodegraph/nodedefinition/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ComputeNodeGraph](computenodegraph.md)
- [ComputeNodeGraph.Assembly](computenodegraph/assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](computenodegraph/pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](computenodegraph/pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.Library](computenodegraph/library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](computenodegraph/libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition)*