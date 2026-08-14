# ShaderGraph

**Framework**: RealityKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ShaderGraph
```

## Topics

### Classes
- [ShaderGraph.NodeLibrary](shadergraph/nodelibrary.md)
  A catalog of node definitions supported by RealityKit.
### Structures
- [ShaderGraph.Edge](shadergraph/edge.md)
  Represents a connection between two nodes in a shader graph.
- [ShaderGraph.Node](shadergraph/node.md)
- [ShaderGraph.NodeDefinition](shadergraph/nodedefinition.md)
  A description of a node type supported by RealityKit, including its inputs, outputs, and platform availability.
### Initializers
- [convenience init(from: Data) throws](shadergraph/init(from:).md)
  Creates a graph from data previously produced by [`encode()`](shadergraph/encode().md).
- [init(named: String, inputs: [ShaderGraph.NodeDefinition.Input], outputs: [ShaderGraph.NodeDefinition.Output]) throws](shadergraph/init(named:inputs:outputs:).md)
  Creates a shader graph with the given name, inputs, and outputs.
- [init(named: String, inputs: [ShaderGraph.NodeDefinition.Input], outputs: [ShaderGraph.NodeDefinition.Output], nodeLibrary: ShaderGraph.NodeLibrary) throws](shadergraph/init(named:inputs:outputs:nodelibrary:).md)
  Creates a shader graph with the given name, inputs, and outputs.
### Instance Properties
- [var arguments: ShaderGraph.Node](shadergraph/arguments.md)
  The virtual node representing this graph’s inputs.
- [var edges: [ShaderGraph.Edge]](shadergraph/edges.md)
- [var functionConstantInputs: [String]](shadergraph/functionconstantinputs.md)
  The names of graph inputs whose values are baked in at program compilation time.
- [var inputs: [ShaderGraph.NodeDefinition.Input]](shadergraph/inputs.md)
  The declared input ports of this graph.
- [var nodes: [String : ShaderGraph.Node]](shadergraph/nodes.md)
  All nodes in the graph, keyed by node name.
- [var outputs: [ShaderGraph.NodeDefinition.Output]](shadergraph/outputs.md)
  The declared output ports of this graph.
- [var primvarMappings: [String : ShaderGraph.TextureCoordinate]](shadergraph/primvarmappings.md)
  Maps primvar names used in this graph to texture coordinate channels.
- [var results: ShaderGraph.Node](shadergraph/results.md)
  The virtual node representing this graph’s outputs.
### Instance Methods
- [func addConstant(ShaderGraph.Value) throws -> String](shadergraph/addconstant(_:).md)
- [func addConstant(ShaderGraph.Value, named: String) throws -> String](shadergraph/addconstant(_:named:).md)
- [func addEdge(ShaderGraph.Edge) throws](shadergraph/addedge(_:).md)
  Adds an edge to the graph.
- [func addNode(ShaderGraph.Node) throws -> String](shadergraph/addnode(_:).md)
  Adds a node to the graph and returns its name.
- [func canAddEdge(ShaderGraph.Edge) -> Bool](shadergraph/canaddedge(_:).md)
  Returns whether an edge can be added to the graph.
- [func canAddNode(ShaderGraph.Node) -> Bool](shadergraph/canaddnode(_:).md)
  Returns whether a node can be added to the graph.
- [func connect(_:outputPort:to:inputPort:)](shadergraph/connect(_:outputport:to:inputport:).md)
  Connect a node with a given output, to a node with a given input. If outputPort is nil, the first output on outputNode is used.
- [func containsEdge(ShaderGraph.Edge) -> Bool](shadergraph/containsedge(_:).md)
  Returns whether the graph contains an edge equal to the given edge.
- [func encode() throws -> Data](shadergraph/encode.md)
  Encodes the graph into a binary representation.
- [func removeEdge(ShaderGraph.Edge) throws](shadergraph/removeedge(_:).md)
  Removes an edge from the graph.
- [func removeNode(String) throws](shadergraph/removenode(_:).md)
- [func replace(nodes: [String : ShaderGraph.Node], edges: [ShaderGraph.Edge]) throws](shadergraph/replace(nodes:edges:).md)
  Replaces all nodes and edges in the graph.
- [func updateNode(ShaderGraph.Node, forKey: String) throws](shadergraph/updatenode(_:forkey:).md)
  Replaces the node stored under the given name.
- [func validate() -> Bool](shadergraph/validate.md)
  Checks whether the graph is well-formed without producing a Metal library.
- [func validateAddingEdge(ShaderGraph.Edge) throws](shadergraph/validateaddingedge(_:).md)
  Validates that an edge can be added to the graph without adding it, throwing a descriptive error if not.
- [func validateAddingNode(ShaderGraph.Node) throws](shadergraph/validateaddingnode(_:).md)
  Validates that a node can be added to the graph without adding it, throwing a descriptive error if not.
### Subscripts
- [subscript(String) -> ShaderGraph.Node?](shadergraph/subscript(_:).md)
### Type Aliases
- [ShaderGraph.EdgeError](shadergraph/edgeerror.md)
- [ShaderGraph.EdgeType](shadergraph/edgetype.md)
- [ShaderGraph.NodeError](shadergraph/nodeerror.md)
- [ShaderGraph.NodeKey](shadergraph/nodekey.md)
- [ShaderGraph.NodeType](shadergraph/nodetype.md)
### Enumerations
- [ShaderGraph.DataType](shadergraph/datatype.md)
- [ShaderGraph.TextureCoordinate](shadergraph/texturecoordinate.md)
- [ShaderGraph.Value](shadergraph/value.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph)*