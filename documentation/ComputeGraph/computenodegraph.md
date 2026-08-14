# ComputeNodeGraph

**Framework**: Compute Graph  
**Kind**: struct

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
struct ComputeNodeGraph
```

## Topics

### Classes
- [ComputeNodeGraph.Library](computenodegraph/library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
### Structures
- [ComputeNodeGraph.ArrayDefinition](computenodegraph/arraydefinition.md)
- [ComputeNodeGraph.Assembly](computenodegraph/assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.DataType](computenodegraph/datatype.md)
- [ComputeNodeGraph.Edge](computenodegraph/edge.md)
- [ComputeNodeGraph.LibraryReference](computenodegraph/libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.
- [ComputeNodeGraph.Metadata](computenodegraph/metadata.md)
- [ComputeNodeGraph.Node](computenodegraph/node.md)
- [ComputeNodeGraph.NodeDefinition](computenodegraph/nodedefinition.md)
- [ComputeNodeGraph.Pipelines](computenodegraph/pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](computenodegraph/pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.PointerDefinition](computenodegraph/pointerdefinition.md)
- [ComputeNodeGraph.PortDefinition](computenodegraph/portdefinition.md)
- [ComputeNodeGraph.SamplerSettings](computenodegraph/samplersettings.md)
- [ComputeNodeGraph.Scope](computenodegraph/scope.md)
  A scope is a named region of memory, indicating where a value lives
- [ComputeNodeGraph.Stage](computenodegraph/stage.md)
  An execution context within a compute node graph that groups related nodes into a processing phase.
- [ComputeNodeGraph.StateDefinition](computenodegraph/statedefinition.md)
  A declaration of a named state value and where it lives in the simulation.
- [ComputeNodeGraph.StructureDefinition](computenodegraph/structuredefinition.md)
  A named structure type, pairing a type name with its in-memory layout.
- [ComputeNodeGraph.StructureLayout](computenodegraph/structurelayout.md)
- [ComputeNodeGraph.SwizzleChannels](computenodegraph/swizzlechannels.md)
### Initializers
- [init()](computenodegraph/init.md)
- [init(data: Data) throws](computenodegraph/init(data:).md)
  Creates a graph by decoding a computegraph.
### Instance Properties
- [var edges: [ComputeNodeGraph.Edge]](computenodegraph/edges.md)
- [var nodes: [ComputeNodeGraph.NodeID : ComputeNodeGraph.Node]](computenodegraph/nodes.md)
### Instance Methods
- [func addEdge(ComputeNodeGraph.Edge) throws](computenodegraph/addedge(_:).md)
- [func addNode(ComputeNodeGraph.Node) throws -> ComputeNodeGraph.NodeID](computenodegraph/addnode(_:).md)
  Adds a node to the graph.
- [func canAddEdge(ComputeNodeGraph.Edge) -> Bool](computenodegraph/canaddedge(_:).md)
  Returns whether the given edge can be added to the graph.
- [func canAddNode(ComputeNodeGraph.Node) -> Bool](computenodegraph/canaddnode(_:).md)
  Returns whether the given node can be added to the graph.
- [func contains(edge: ComputeNodeGraph.Edge) -> Bool](computenodegraph/contains(edge:).md)
  Returns whether the graph contains the given edge.
- [func contains(node: ComputeNodeGraph.NodeID) -> Bool](computenodegraph/contains(node:).md)
  Returns whether the graph contains a node with the given key.
- [func data(using: ComputeNodeGraph.Format) throws -> Data](computenodegraph/data(using:).md)
  Returns the graph encoded in the specified format.
- [func removeEdge(ComputeNodeGraph.Edge) -> Bool](computenodegraph/removeedge(_:).md)
  Removes an edge from the graph.
- [func removeNode(ComputeNodeGraph.NodeID) throws](computenodegraph/removenode(_:).md)
  Removes a node from the graph.
- [func replaceAll(nodes: [ComputeNodeGraph.NodeID : ComputeNodeGraph.Node], edges: [ComputeNodeGraph.Edge]) throws](computenodegraph/replaceall(nodes:edges:).md)
  Replaces all nodes and edges in the graph with the provided collections.
- [func updateNode(ComputeNodeGraph.Node, forKey: ComputeNodeGraph.NodeID) throws](computenodegraph/updatenode(_:forkey:).md)
  Updates an existing node in the graph.
### Subscripts
- [subscript(ComputeNodeGraph.NodeID) -> ComputeNodeGraph.Node?](computenodegraph/subscript(_:).md)
  Accesses the node associated with the given key.
### Type Aliases
- [ComputeNodeGraph.NodeID](computenodegraph/nodeid.md)
### Enumerations
- [ComputeNodeGraph.Format](computenodegraph/format.md)
  A serialization format used to encode a compute node graph.
- [ComputeNodeGraph.Port](computenodegraph/port.md)
- [ComputeNodeGraph.StateType](computenodegraph/statetype.md)
  The shape of a value stored in a compute graph’s state.
- [ComputeNodeGraph.Topology](computenodegraph/topology.md)
  The primitive topology used to assemble output geometry for an output stage.
- [ComputeNodeGraph.ValueType](computenodegraph/valuetype.md)
  Describes the storage and layout of a port’s value, ranging from Metal primitives and structures to opaque references and stateful bindings.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph)*