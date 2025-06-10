# MTLIOPriority

**Framework**: Metal  
**Kind**: enum

Designates the priority for a new input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLIOPriority
```

#### Overview

Set a new input/output command queue’s priority that you create with a [`MTLIOCommandQueueDescriptor`](mtliocommandqueuedescriptor.md) instance by setting its [`priority`](mtliocommandqueuedescriptor/priority.md) property. Create a queue that minimizes an asset’s loading latency by setting a descriptor’s priority to [`MTLIOPriority.high`](mtliopriority/high.md).

## Topics

### I/O Command Queue Priorities
- [MTLIOPriority.normal](mtliopriority/normal.md)
  Designates the normal priority for a new input/output command queue.
- [MTLIOPriority.low](mtliopriority/low.md)
  Designates the low priority for a new input/output command queue.
- [MTLIOPriority.high](mtliopriority/high.md)
  Sets a new input/output command queue’s priority to a high priority.
### Initializers
- [init?(rawValue: Int)](mtliopriority/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLIOCommandQueue](mtliocommandqueue.md)
  A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [class MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md)
  A configuration template you use to create a new input/output command queue.
- [enum MTLIOCommandQueueType](mtliocommandqueuetype.md)
  Designates the queue type for a new input/output command queue.
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliopriority)*