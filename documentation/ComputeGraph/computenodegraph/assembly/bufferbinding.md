# ComputeNodeGraph.Assembly.BufferBinding

**Framework**: Compute Graph  
**Kind**: struct

Describes how a Metal buffer is bound to a compute pipeline stage.

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
struct BufferBinding
```

#### Overview

A buffer binding pairs an [`ComputeNodeGraph.Assembly.Attachment`](computenodegraph/assembly/attachment.md) (how the buffer is connected to the graph) with an optional [`ComputeNodeGraph.StateType`](computenodegraph/statetype.md) describing the element layout of the buffer’s contents.

## Topics

### Initializers
- [init(attachment: ComputeNodeGraph.Assembly.Attachment, type: ComputeNodeGraph.StateType?)](computenodegraph/assembly/bufferbinding/init(attachment:type:).md)
### Instance Properties
- [var attachment: ComputeNodeGraph.Assembly.Attachment](computenodegraph/assembly/bufferbinding/attachment.md)
  The attachment point that provides this buffer.
- [var type: ComputeNodeGraph.StateType?](computenodegraph/assembly/bufferbinding/type.md)
  The element type stored in the buffer, or `nil` if untyped.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/bufferbinding)*