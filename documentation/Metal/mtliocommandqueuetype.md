# MTLIOCommandQueueType

**Framework**: Metal  
**Kind**: enum

Designates the queue type for a new input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLIOCommandQueueType
```

## Topics

### I/O Command Queue Types
- [MTLIOCommandQueueType.concurrent](mtliocommandqueuetype/concurrent.md)
  Sets a new input/output command queue’s type to a queue that runs commands concurrently.
- [MTLIOCommandQueueType.serial](mtliocommandqueuetype/serial.md)
  Sets a new input/output command queue’s type to a queue that runs commands serially.
### Initializers
- [init?(rawValue: Int)](mtliocommandqueuetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIOCommandQueue](mtliocommandqueue.md)
  A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [class MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md)
  A configuration template you use to create a new input/output command queue.
- [enum MTLIOPriority](mtliopriority.md)
  Designates the priority for a new input/output command queue.
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueuetype)*