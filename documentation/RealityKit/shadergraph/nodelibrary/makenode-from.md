# makeNode(from:)

**Framework**: RealityKit  
**Kind**: method

Creates a node instance of the given definition.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeNode(from definition: ShaderGraph.NodeDefinition) throws -> ShaderGraph.Node
```

#### Return Value

A [`ShaderGraph.Node`](shadergraph/node.md) that can be added to a [`ShaderGraph`](shadergraph.md).

#### Discussion

> **Note**: If the definition does not belong to this library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodelibrary/makenode(from:))*