# MTLIOScratchBufferAllocator

**Framework**: Metal  
**Kind**: protocol

A protocol your app implements to provide scratch memory to an input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIOScratchBufferAllocator : NSObjectProtocol
```

#### Overview

An allocator returns instances of [`MTLIOScratchBuffer`](mtlioscratchbuffer.md), another type your app implements.

## Topics

### Providing Scratch Memory to a Queue
- [func makeScratchBuffer(minimumSize: Int) -> (any MTLIOScratchBuffer)?](mtlioscratchbufferallocator/makescratchbuffer(minimumsize:).md)
  Creates a scratch memory buffer for an input/output command queue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLIOCommandQueue](mtliocommandqueue.md)
  A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [class MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md)
  A configuration template you use to create a new input/output command queue.
- [enum MTLIOPriority](mtliopriority.md)
  Designates the priority for a new input/output command queue.
- [enum MTLIOCommandQueueType](mtliocommandqueuetype.md)
  Designates the queue type for a new input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioscratchbufferallocator)*