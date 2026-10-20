# ComputeNodeGraph.Port.Address

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

A location of a specific port on a node, identified by the node and the port’s index.

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
struct Address
```

## Topics

### Initializers
- [init(node: ComputeNodeGraph.NodeID, index: Int)](./address/init%28node,index%29.md)
### Instance Properties
- [var index: Int](./address/index.md)
  The index of the port within the node’s input or output list.
- [var node: ComputeNodeGraph.NodeID](./address/node.md)
  The node that owns this port.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/address)*