# makeNode(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates a node instance of the given definition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makeNode(from definition: ShaderGraph.NodeDefinition) throws -> ShaderGraph.Node
```

#### Return Value

A [`ShaderGraph.Node`](../node.md) that can be added to a [`ShaderGraph`](../../shadergraph.md).

#### Discussion

> **Throws**: If the definition does not belong to this library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodelibrary/makenode(from:))*