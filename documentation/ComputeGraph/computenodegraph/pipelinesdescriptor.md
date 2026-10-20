# ComputeNodeGraph.PipelinesDescriptor

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.

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
struct PipelinesDescriptor
```

#### Overview

Use a descriptor when you need explicit control over pipeline compilation — for example, to supply Metal libraries from multiple bundles or to enable debug draw. Pass the configured descriptor to `ComputeNodeGraph.Pipelines/init(descriptor:)` to compile.

```swift
var descriptor = ComputeNodeGraph.PipelinesDescriptor(assembly: assembly)
descriptor.addLibrary(myMTLLibrary, bundle: "com.example.MyEffects")
descriptor.options.debugDraw = true
let pipelines = try await ComputeNodeGraph.Pipelines(descriptor: descriptor)
```

## Topics

### Initializers
- [init(assembly: ComputeNodeGraph.Assembly)](./pipelinesdescriptor/init%28assembly%29.md)
  Creates a descriptor configured for the given graph assembly.
### Instance Properties
- [var assembly: ComputeNodeGraph.Assembly](./pipelinesdescriptor/assembly.md)
  The assembled compute graph layout that defines the graph’s buffer, uniform, and texture configuration.
- [var libraries: [ComputeNodeGraph.LibraryReference]](./pipelinesdescriptor/libraries.md)
  The Metal libraries that provide shader function implementations for the graph’s nodes.
- [var options: ComputeNodeGraph.Pipelines.Options](./pipelinesdescriptor/options.md)
  Options controlling pipeline compilation, such as whether debug draw is enabled.
### Instance Methods
- [func addLibrary(any MTLLibrary, bundle: String?)](./pipelinesdescriptor/addlibrary%28_,bundle%29.md)
- [func setLibrary(ComputeNodeGraph.Library)](./pipelinesdescriptor/setlibrary%28_%29.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Graph definition and assembly
- [struct ComputeNodeGraph](../computenodegraph.md)
- [ComputeNodeGraph.Assembly](./assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](./pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.NodeDefinition](./nodedefinition.md)
- [ComputeNodeGraph.Library](./library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](./libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelinesdescriptor)*