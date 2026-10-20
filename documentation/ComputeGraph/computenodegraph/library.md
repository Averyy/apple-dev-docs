# ComputeNodeGraph.Library

**Framework**: Compute Graph  
**Kind**: class  
**Role**: Class

A class defining a library of node definitions that can be added to a ComputeNodeGraph

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
final class Library
```

#### Overview

A Library contains definitions and also stores MTLFunction implementations for built-in nodes and you can construct new libraries containing nodes you provide.

These nodes are functions implemented using the Metal Shading Language and annotated with the `[[stitchable]]` attribute.

## Topics

### Initializers
- [init()](./library/init%28%29.md)
  Creates a new empty library.
- [convenience init?(bundle: Bundle)](./library/init%28bundle%29.md)
  Creates a library from the Metal default library in the given bundle, if available.
- [convenience init(from: any MTLLibrary, bundleIdentifier: String?)](./library/init%28from,bundleidentifier%29.md)
  Creates a library by extracting node definitions from a Metal library.
### Instance Properties
- [var definitions: [ComputeNodeGraph.NodeDefinition]](./library/definitions.md)
  The collection of all node definitions available in this library.
### Instance Methods
- [func definition(named: String, in: String?) -> ComputeNodeGraph.NodeDefinition?](./library/definition%28named,in%29.md)
  Returns the first node definition with the given name, or `nil` if none is found.
- [func definition(stage: ComputeNodeGraph.Stage) -> ComputeNodeGraph.NodeDefinition?](./library/definition%28stage%29.md)
  Returns a definition for the given stage.
- [func definitionsMatching(input: ComputeNodeGraph.ValueType) -> [ComputeNodeGraph.NodeDefinition]](./library/definitionsmatching%28input%29.md)
  Returns all definitions that have at least one input matching the given value type.
- [func definitionsMatching(inputs: [ComputeNodeGraph.ValueType]) -> [ComputeNodeGraph.NodeDefinition]](./library/definitionsmatching%28inputs%29.md)
  Returns all definitions whose user-editable inputs, in order, match the given value types.
- [func definitionsMatching(output: ComputeNodeGraph.ValueType) -> [ComputeNodeGraph.NodeDefinition]](./library/definitionsmatching%28output%29.md)
  Returns all definitions that have at least one output matching the given value type.
- [func merge(contentsOf: ComputeNodeGraph.Library)](./library/merge%28contentsof%29.md)
  Merges nodes from specified library into this library.
### Type Properties
- [static let shared: ComputeNodeGraph.Library](./library/shared.md)

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
- [ComputeNodeGraph.PipelinesDescriptor](./pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](./nodedefinition.md)
- [ComputeNodeGraph.LibraryReference](./libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library)*