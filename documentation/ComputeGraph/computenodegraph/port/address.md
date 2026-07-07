# ComputeNodeGraph.Port.Address

**Framework**: Compute Graph  
**Kind**: struct

A location of a specific port on a node, identified by the node and the port’s index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/address)*