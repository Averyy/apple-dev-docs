# ComputeNodeGraph.Node.Kind

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [case grouping(nodes: [ComputeNodeGraph.NodeID])](./kind-swift.enum/grouping%28nodes%29.md)
  Node is a visual grouping of nodes. This can be presented as, for example, a box around the nodes, indicating that they are related, but without changing their structure.
- [ComputeNodeGraph.Node.Kind.primitive](./kind-swift.enum/primitive.md)
  Node is standalone operation
- [case sequence(nodes: [ComputeNodeGraph.NodeID])](./kind-swift.enum/sequence%28nodes%29.md)
  Node is a sequence of nodes, which have implicit flow dependencies between them.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/node/kind-swift.enum)*