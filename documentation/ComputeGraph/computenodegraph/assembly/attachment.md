# ComputeNodeGraph.Assembly.Attachment

**Framework**: Compute Graph  
**Kind**: enum  
**Role**: Enumeration

Identifies where a resource is attached in the compute graph.

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
enum Attachment
```

#### Overview

Each buffer and texture bound to a compute pipeline is sourced from a specific attachment point: the graph itself, or a named input or output port on a node.

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Assembly.Attachment.graph](./attachment/graph.md)
  The resource is owned by the graph and shared across all stages.
- [ComputeNodeGraph.Assembly.Attachment.input(_:)](./attachment/input%28_%29.md)
  The resource is read by an input port at the given address.
- [ComputeNodeGraph.Assembly.Attachment.output(_:)](./attachment/output%28_%29.md)
  The resource is produced by an output port at the given address.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/attachment)*