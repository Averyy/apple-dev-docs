# MTLCommandBufferStatus.scheduled

**Framework**: Metal  
**Kind**: case

A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case scheduled
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

See the [`MTLCommandBuffer`](mtlcommandbuffer.md) protocol’s [`status`](mtlcommandbuffer/status.md) property for more information.

## See Also

- [MTLCommandBufferStatus.notEnqueued](mtlcommandbufferstatus/notenqueued.md)
  A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it.
- [MTLCommandBufferStatus.enqueued](mtlcommandbufferstatus/enqueued.md)
  A command buffer’s second state, which indicates its command queue is reserving a place for it.
- [MTLCommandBufferStatus.committed](mtlcommandbufferstatus/committed.md)
  A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies.
- [MTLCommandBufferStatus.completed](mtlcommandbufferstatus/completed.md)
  A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems.
- [MTLCommandBufferStatus.error](mtlcommandbufferstatus/error.md)
  A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/scheduled)*