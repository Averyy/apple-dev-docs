# ShaderGraph.NodeLibrary

**Framework**: RealityKit  
**Kind**: class

A catalog of node definitions supported by RealityKit.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class NodeLibrary
```

#### Overview

Use a library to discover available [`ShaderGraph.NodeDefinition`](shadergraph/nodedefinition.md) values and add instances of them to a [`ShaderGraph`](shadergraph.md).

```swift
let library = ShaderGraph.NodeLibrary(version: .materialX138)
let pbrDef = library.definition(named: "ND_realitykit_pbr_surfaceshader")!
let pbrNode = try library.makeNode(from: pbrDef)
let pbr = graph.addNode(pbrNode)
```

## Topics

### Structures
- [ShaderGraph.NodeLibrary.Version](shadergraph/nodelibrary/version.md)
### Initializers
- [init(version: ShaderGraph.NodeLibrary.Version)](shadergraph/nodelibrary/init(version:).md)
  Creates a library containing all node definitions supported by RealityKit for the given library version.
### Instance Properties
- [var definitions: some Collection<ShaderGraph.NodeDefinition>](shadergraph/nodelibrary/definitions.md)
  All node definitions in this library.
### Instance Methods
- [func definition(named: String) -> ShaderGraph.NodeDefinition?](shadergraph/nodelibrary/definition(named:).md)
  Returns the definition with the given name, or `nil` if no such definition exists in this library.
- [func definitions(function: String, input: ShaderGraph.DataType) -> [ShaderGraph.NodeDefinition]](shadergraph/nodelibrary/definitions(function:input:).md)
  Returns all definitions that implement the given function with the specified input type.
- [func definitions(function:inputs:)](shadergraph/nodelibrary/definitions(function:inputs:).md)
  Returns all definitions that implement the given function with the specified input types, in order.
- [func definitions(function: String, output: ShaderGraph.DataType) -> [ShaderGraph.NodeDefinition]](shadergraph/nodelibrary/definitions(function:output:).md)
  Returns all definitions that implement the given function with the specified output type.
- [func makeNode(from: ShaderGraph.NodeDefinition) throws -> ShaderGraph.Node](shadergraph/nodelibrary/makenode(from:).md)
  Creates a node instance of the given definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodelibrary)*