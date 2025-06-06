# priority

**Framework**: Metal  
**Kind**: property

Configures the priority for a new input/output command queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var priority: MTLIOPriority { get set }
```

## See Also

- [var type: MTLIOCommandQueueType](mtliocommandqueuedescriptor/type.md)
  Configures the queue type for a new input/output command queue.
- [var maxCommandsInFlight: Int](mtliocommandqueuedescriptor/maxcommandsinflight.md)
  Sets the largest number of individual commands that an input/output command queue can run at a time.
- [var maxCommandBufferCount: Int](mtliocommandqueuedescriptor/maxcommandbuffercount.md)
  Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/priority)*