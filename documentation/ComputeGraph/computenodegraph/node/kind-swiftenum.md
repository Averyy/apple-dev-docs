# ComputeNodeGraph.Node.Kind

**Framework**: ComputeGraph  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [case grouping(nodes: [ComputeNodeGraph.NodeID])](computenodegraph/node/kind-swift.enum/grouping(nodes:).md)
  Node is a visual grouping of nodes. This can be presented as, for example, a box around the nodes, indicating that they are related, but without changing their structure.
- [ComputeNodeGraph.Node.Kind.primitive](computenodegraph/node/kind-swift.enum/primitive.md)
  Node is standalone operation
- [case sequence(nodes: [ComputeNodeGraph.NodeID])](computenodegraph/node/kind-swift.enum/sequence(nodes:).md)
  Node is a sequence of nodes, which have implicit flow dependencies between them.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/node/kind-swift.enum)*