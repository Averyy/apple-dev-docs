# ShaderGraph.NodeDefinition

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A description of a node type supported by RealityKit, including its inputs, outputs, and platform availability.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct NodeDefinition
```

## Overview

Obtain definitions from a [`ShaderGraph.NodeLibrary`](./nodelibrary.md) and use them to add nodes to a [`ShaderGraph`](../shadergraph.md).

## Topics

### Structures
- [ShaderGraph.NodeDefinition.Input](./nodedefinition/input.md)
- [ShaderGraph.NodeDefinition.Output](./nodedefinition/output.md)
- [ShaderGraph.NodeDefinition.SemanticType](./nodedefinition/semantictype.md)
### Instance Properties
- [var availability: [ShaderGraph.NodeDefinition.Platform : ShaderGraph.NodeDefinition.Availability]](./nodedefinition/availability-swift.property.md)
  The availability of this node definition on each platform.
- [var functionalName: String](./nodedefinition/functionalname.md)
  The name of the functional operation this definition implements.
- [var group: String?](./nodedefinition/group.md)
  The category this definition belongs to, or `nil` if uncategorized.
- [var inputs: [ShaderGraph.NodeDefinition.Input]](./nodedefinition/inputs.md)
  The input ports accepted by this node definition.
- [var name: String](./nodedefinition/name.md)
  The unique identifier for this node definition.
- [var outputs: [ShaderGraph.NodeDefinition.Output]](./nodedefinition/outputs.md)
  The output ports produced by this node definition.
### Instance Methods
- [func isAvailable(on: ShaderGraph.NodeDefinition.Platform, version: OperatingSystemVersion?) -> Bool](./nodedefinition/isavailable%28on,version%29.md)
  Returns whether this node definition is available on a given platform and OS version.
### Enumerations
- [ShaderGraph.NodeDefinition.Availability](./nodedefinition/availability-swift.enum.md)
- [ShaderGraph.NodeDefinition.Platform](./nodedefinition/platform.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition)*