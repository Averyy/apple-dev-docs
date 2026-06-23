# ShaderGraph.NodeDefinition

**Framework**: RealityKit  
**Kind**: struct

A description of a node type supported by RealityKit, including its inputs, outputs, and platform availability.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NodeDefinition
```

#### Overview

Obtain definitions from a [`ShaderGraph.NodeLibrary`](shadergraph/nodelibrary.md) and use them to add nodes to a [`ShaderGraph`](shadergraph.md).

## Topics

### Structures
- [ShaderGraph.NodeDefinition.Input](shadergraph/nodedefinition/input.md)
- [ShaderGraph.NodeDefinition.Output](shadergraph/nodedefinition/output.md)
- [ShaderGraph.NodeDefinition.SemanticType](shadergraph/nodedefinition/semantictype.md)
### Instance Properties
- [var availability: [ShaderGraph.NodeDefinition.Platform : ShaderGraph.NodeDefinition.Availability]](shadergraph/nodedefinition/availability-swift.property.md)
  The availability of this node definition on each platform.
- [var functionalName: String](shadergraph/nodedefinition/functionalname.md)
  The name of the functional operation this definition implements.
- [var group: String?](shadergraph/nodedefinition/group.md)
  The category this definition belongs to, or `nil` if uncategorized.
- [var inputs: [ShaderGraph.NodeDefinition.Input]](shadergraph/nodedefinition/inputs.md)
  The input ports accepted by this node definition.
- [var name: String](shadergraph/nodedefinition/name.md)
  The unique identifier for this node definition.
- [var outputs: [ShaderGraph.NodeDefinition.Output]](shadergraph/nodedefinition/outputs.md)
  The output ports produced by this node definition.
### Instance Methods
- [func isAvailable(on: ShaderGraph.NodeDefinition.Platform, version: OperatingSystemVersion?) -> Bool](shadergraph/nodedefinition/isavailable(on:version:).md)
  Returns whether this node definition is available on a given platform and OS version.
### Enumerations
- [ShaderGraph.NodeDefinition.Availability](shadergraph/nodedefinition/availability-swift.enum.md)
- [ShaderGraph.NodeDefinition.Platform](shadergraph/nodedefinition/platform.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition)*