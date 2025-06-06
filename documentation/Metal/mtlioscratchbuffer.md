# MTLIOScratchBuffer

**Framework**: Metal  
**Kind**: protocol

A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIOScratchBuffer : NSObjectProtocol
```

#### Overview

Your app can reintegrate a [`MTLIOScratchBuffer`](mtlioscratchbuffer.md) instance’s underlying memory back into a memory pool by overriding your type’s [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) method. The system calls the method when an input/output command queue no longer needs a scratch buffer.

## Topics

### Wrapping a Buffer
- [var buffer: any MTLBuffer](mtlioscratchbuffer/buffer.md)
  A Metal buffer that serves as scratch memory for an input/output command queue.

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
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioscratchbuffer)*