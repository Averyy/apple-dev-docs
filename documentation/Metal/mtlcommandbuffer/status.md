# status

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The command buffer’s current state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var status: MTLCommandBufferStatus { get }
```

## Mentions

- [Preparing Your Metal App to Run in the Background](preparing-your-metal-app-to-run-in-the-background.md)
- [Setting Up a Command Structure](setting-up-a-command-structure.md)

#### Discussion

Each command buffer can be in any one of the following states:

| State | Meaning |
| --- | --- |
| [`MTLCommandBufferStatus.notEnqueued`](mtlcommandbufferstatus/notenqueued.md) | A command buffer’s initial state, which indicates its command queue isn’t reserving a place for it. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can modify a command buffer in this state by encoding commands to it, or by adding a state change handler. |
| [`MTLCommandBufferStatus.enqueued`](mtlcommandbufferstatus/enqueued.md) | A command buffer’s second state, which indicates its command queue is reserving a place for it. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can modify a command buffer in this state by encoding commands to it, or by adding a state change handler. |
| [`MTLCommandBufferStatus.committed`](mtlcommandbufferstatus/committed.md) | A command buffer’s third state, which indicates the command queue is preparing to schedule the command buffer by resolving its dependencies. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can’t modify a command buffer in this state. |
| [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md) | A command buffer’s fourth state, which indicates the command buffer has its resources ready and is waiting for the GPU to run its commands. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You can’t modify a command buffer in this state. |
| [`MTLCommandBufferStatus.completed`](mtlcommandbufferstatus/completed.md) | A command buffer’s successful, final state, which indicates the GPU finished running the command buffer’s commands without any problems. |
| [`MTLCommandBufferStatus.error`](mtlcommandbufferstatus/error.md) | A command buffer’s unsuccessful, final state, which indicates the GPU stopped running the buffer’s commands because of a runtime issue. |

The first two states ([`MTLCommandBufferStatus.notEnqueued`](mtlcommandbufferstatus/notenqueued.md) and [`MTLCommandBufferStatus.enqueued`](mtlcommandbufferstatus/enqueued.md)) both indicate that you can encode commands to the command buffer. You do this by creating an encoder that indirectly adds commands for a pass (see [`Command Encoder Factory Methods`](command-encoder-factory-methods.md)) to the command buffer. Command buffers also have some methods that directly encode commands between passes, such as [`encodeSignalEvent(_:value:)`](mtlcommandbuffer/encodesignalevent(_:value:).md) and [`present(_:)`](mtlcommandbuffer/present(_:).md).

Each command buffer’s state can only change to a state below it in the table, and ends its life cycle at either [`MTLCommandBufferStatus.completed`](mtlcommandbufferstatus/completed.md) or [`MTLCommandBufferStatus.error`](mtlcommandbufferstatus/error.md).

## See Also

- [enum MTLCommandBufferStatus](mtlcommandbufferstatus.md)
  The discrete states for a command buffer that represent its life cycle stages.
- [Command Buffer Debugging](command-buffer-debugging.md)
  Properties and methods for programmatically debugging runtime issues with a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/status)*