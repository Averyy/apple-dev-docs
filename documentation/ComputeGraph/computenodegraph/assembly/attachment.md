# ComputeNodeGraph.Assembly.Attachment

**Framework**: ComputeGraph  
**Kind**: enum

Identifies where a resource is attached in the compute graph.

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
enum Attachment
```

#### Overview

Each buffer and texture bound to a compute pipeline is sourced from a specific attachment point: the graph itself, or a named input or output port on a node.

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Assembly.Attachment.graph](computenodegraph/assembly/attachment/graph.md)
  The resource is owned by the graph and shared across all stages.
- [ComputeNodeGraph.Assembly.Attachment.input(_:)](computenodegraph/assembly/attachment/input(_:).md)
  The resource is read by an input port at the given address.
- [ComputeNodeGraph.Assembly.Attachment.output(_:)](computenodegraph/assembly/attachment/output(_:).md)
  The resource is produced by an output port at the given address.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/attachment)*