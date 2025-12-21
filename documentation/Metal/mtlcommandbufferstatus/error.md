# MTLCommandBufferStatus.error

**Framework**: Metal  
**Kind**: case

A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case error
```

## Mentions

- [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md)

#### Discussion

See the [`MTLCommandBuffer`](mtlcommandbuffer.md) protocol’s [`status`](mtlcommandbuffer/status.md) property for more information. When a command buffer’s status is equal to [`MTLCommandBufferStatus.error`](mtlcommandbufferstatus/error.md), check its [`error`](mtlcommandbuffer/error.md) property for more details about the issue. See [`Command buffer debugging`](command-buffer-debugging.md) for more methods properties that can help you identify the issue.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/error)*