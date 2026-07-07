# addNode(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a node to the graph and returns its name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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