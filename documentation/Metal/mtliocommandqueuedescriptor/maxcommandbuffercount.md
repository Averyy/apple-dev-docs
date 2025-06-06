# maxCommandBufferCount

**Framework**: Metal  
**Kind**: property

Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxCommandBufferCount: Int { get set }
```

#### Discussion

The input/output command buffers that count against this limit are those that are currently executing in a queue or waiting to execute. The command buffers that have finished executing no longer count against this limit.

## See Also

- [var priority: MTLIOPriority](mtliocommandqueuedescriptor/priority.md)
  Configures the priority for a new input/output command queue.
- [var type: MTLIOCommandQueueType](mtliocommandqueuedescriptor/type.md)
  Configures the queue type for a new input/output command queue.
- [var maxCommandsInFlight: Int](mtliocommandqueuedescriptor/maxcommandsinflight.md)
  Sets the largest number of individual commands that an input/output command queue can run at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/maxcommandbuffercount)*