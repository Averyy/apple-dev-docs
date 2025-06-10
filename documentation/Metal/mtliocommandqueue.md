# MTLIOCommandQueue

**Framework**: Metal  
**Kind**: protocol

A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIOCommandQueue : NSObjectProtocol, Sendable
```

#### Overview

Use an input/output command queue to submit commands, in command buffers, that load assets from the file system directly into GPU resources. Your app can then use those resources with other commands it submits to an [`MTLCommandQueue`](mtlcommandqueue.md) that comes from the same [`MTLDevice`](mtldevice.md).

You make input/output command queues by creating and configuring an [`MTLIOCommandQueueDescriptor`](mtliocommandqueuedescriptor.md) instance and calling an [`MTLDevice`](mtldevice.md) instance’s [`makeIOCommandQueue(descriptor:)`](mtldevice/makeiocommandqueue(descriptor:).md) method.

## Topics

### Creating a Input/Output Command Buffer
- [func makeCommandBuffer() -> any MTLIOCommandBuffer](mtliocommandqueue/makecommandbuffer.md)
  Creates an input/output command buffer for the command queue.
- [func makeCommandBufferWithUnretainedReferences() -> any MTLIOCommandBuffer](mtliocommandqueue/makecommandbufferwithunretainedreferences.md)
  Creates an input/output command buffer for the command queue that doesn’t retain the instances you pass to its methods.
### Adding a Barrier to the Queue
- [func enqueueBarrier()](mtliocommandqueue/enqueuebarrier.md)
  Appends a barrier that tells the input/output command queue to finish running all in-flight command buffers before running any new command buffers.
### Naming the Queue
- [var label: String?](mtliocommandqueue/label.md)
  An optional name for the input/output command queue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md)
  A configuration template you use to create a new input/output command queue.
- [enum MTLIOPriority](mtliopriority.md)
  Designates the priority for a new input/output command queue.
- [enum MTLIOCommandQueueType](mtliocommandqueuetype.md)
  Designates the queue type for a new input/output command queue.
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueue)*