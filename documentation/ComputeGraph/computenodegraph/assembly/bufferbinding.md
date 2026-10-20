# ComputeNodeGraph.Assembly.BufferBinding

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Describes how a Metal buffer is bound to a compute pipeline stage.

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
struct BufferBinding
```

#### Overview

A buffer binding pairs an [`ComputeNodeGraph.Assembly.Attachment`](./attachment.md) (how the buffer is connected to the graph) with an optional [`ComputeNodeGraph.StateType`](../statetype.md) describing the element layout of the buffer’s contents.

## Topics

### Initializers
- [init(attachment: ComputeNodeGraph.Assembly.Attachment, type: ComputeNodeGraph.StateType?)](./bufferbinding/init%28attachment,type%29.md)
### Instance Properties
- [var attachment: ComputeNodeGraph.Assembly.Attachment](./bufferbinding/attachment.md)
  The attachment point that provides this buffer.
- [var type: ComputeNodeGraph.StateType?](./bufferbinding/type.md)
  The element type stored in the buffer, or `nil` if untyped.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/bufferbinding)*