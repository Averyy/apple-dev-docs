# MTLCommandBufferStatus

**Framework**: Metal  
**Kind**: enum

The discrete states for a command buffer that represent its life cycle stages.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLCommandBufferStatus
```

## Topics

### Command Buffer States
- [MTLCommandBufferStatus.notEnqueued](mtlcommandbufferstatus/notenqueued.md)
  A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it.
- [MTLCommandBufferStatus.enqueued](mtlcommandbufferstatus/enqueued.md)
  A command buffer’s second state, which indicates its command queue is reserving a place for it.
- [MTLCommandBufferStatus.committed](mtlcommandbufferstatus/committed.md)
  A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies.
- [MTLCommandBufferStatus.scheduled](mtlcommandbufferstatus/scheduled.md)
  A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands.
- [MTLCommandBufferStatus.completed](mtlcommandbufferstatus/completed.md)
  A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems.
- [MTLCommandBufferStatus.error](mtlcommandbufferstatus/error.md)
  A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue.
### Initializers
- [init?(rawValue: UInt)](mtlcommandbufferstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: MTLCommandBufferStatus](mtlcommandbuffer/status.md)
  The command buffer’s current state.
- [Command Buffer Debugging](command-buffer-debugging.md)
  Properties and methods for programmatically debugging runtime issues with a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus)*