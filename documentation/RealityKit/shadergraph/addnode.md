# addNode(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a node to the graph and returns its name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
final func addNode(_ node: ShaderGraph.Node) throws -> String
```

#### Return Value

The name used to reference this node in subsequent calls.

#### Discussion

> **Note**: If the node is invalid for this graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/addnode(_:))*