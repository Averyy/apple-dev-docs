# MTLIOCommandQueueDescriptor

**Framework**: Metal  
**Kind**: class

A configuration template you use to create a new input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLIOCommandQueueDescriptor
```

#### Overview

Use this descriptor type to configure the settings of each input/output command queue that you create using [`makeIOCommandQueue(descriptor:)`](mtldevice/makeiocommandqueue(descriptor:).md). To create additional input/output command queues, you can reuse a descriptor instance and optionally reconfigure its properties.

> **Note**:  Changing a descriptor’s properties doesn’t affect command queues you’ve already created with the descriptor.

Create each input/output queue to meet your apps needs by setting the descriptor’s properties.

- Select a queue’s relative level of importance with the [`priority`](mtliocommandqueuedescriptor/priority.md) property.
- Create a queue that runs multiple input/output command buffers in parallel by setting the [`type`](mtliocommandqueuedescriptor/type.md) property to [`MTLIOCommandQueueType.concurrent`](mtliocommandqueuetype/concurrent.md).
- Decide how many individual commands a queue can run simultaneously with the [`maxCommandsInFlight`](mtliocommandqueuedescriptor/maxcommandsinflight.md) property.
- Choose how many command buffers a queue can have waiting to run with [`maxCommandBufferCount`](mtliocommandqueuedescriptor/maxcommandbuffercount.md) property.
- Take control of the queue’s scratch memory allocation by implementing [`MTLIOScratchBufferAllocator`](mtlioscratchbufferallocator.md) and assign an instance of it to the [`scratchBufferAllocator`](mtliocommandqueuedescriptor/scratchbufferallocator.md) property.

## Topics

### Configuring the Input/Output Command Queue
- [var priority: MTLIOPriority](mtliocommandqueuedescriptor/priority.md)
  Configures the priority for a new input/output command queue.
- [var type: MTLIOCommandQueueType](mtliocommandqueuedescriptor/type.md)
  Configures the queue type for a new input/output command queue.
- [var maxCommandsInFlight: Int](mtliocommandqueuedescriptor/maxcommandsinflight.md)
  Sets the largest number of individual commands that an input/output command queue can run at a time.
- [var maxCommandBufferCount: Int](mtliocommandqueuedescriptor/maxcommandbuffercount.md)
  Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.
### Providing your own  a Scratch Buffer
- [var scratchBufferAllocator: (any MTLIOScratchBufferAllocator)?](mtliocommandqueuedescriptor/scratchbufferallocator.md)
  An optional memory allocator that you implement to manage the scratch memory that an input/output command queue requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLIOCommandQueue](mtliocommandqueue.md)
  A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [enum MTLIOPriority](mtliopriority.md)
  Designates the priority for a new input/output command queue.
- [enum MTLIOCommandQueueType](mtliocommandqueuetype.md)
  Designates the queue type for a new input/output command queue.
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal/mtliocommandqueuedescriptor)*