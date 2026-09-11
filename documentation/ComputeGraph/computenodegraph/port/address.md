# ComputeNodeGraph.Port.Address

**Framework**: Compute Graph  
**Kind**: struct

A location of a specific port on a node, identified by the node and the port’s index.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
struct Address
```

## Topics

### Initializers
- [init(node: ComputeNodeGraph.NodeID, index: Int)](computenodegraph/port/address/init(node:index:).md)
### Instance Properties
- [var index: Int](computenodegraph/port/address/index.md)
  The index of the port within the node’s input or output list.
- [var node: ComputeNodeGraph.NodeID](computenodegraph/port/address/node.md)
  The node that owns this port.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/address)*