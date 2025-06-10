# addCompletedHandler(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func addCompletedHandler(_ block: @escaping MTLCommandBufferHandler)
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Setting Up a Command Structure](setting-up-a-command-structure.md)
- [Preparing Your Metal App to Run in the Background](preparing-your-metal-app-to-run-in-the-background.md)

#### Discussion

You can register one or more completion handlers for the same command buffer. The GPU device’s driver (on the CPU) calls the completion handlers after the GPU finishes executing the command buffer.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

For example, you can use the command buffer’s [`gpuEndTime`](mtlcommandbuffer/gpuendtime.md) and [`gpuStartTime`](mtlcommandbuffer/gpustarttime.md) properties to calculate how much time the GPU spends running the command buffer.

The completion handler is also a good place to check the [`status`](mtlcommandbuffer/status.md) property to determine whether the GPU successfully completes the buffer’s commands. If the status is equal to [`MTLCommandBufferStatus.error`](mtlcommandbufferstatus/error.md), you can investigate further by checking the [`error`](mtlcommandbuffer/error.md) and log properties for more details about the issue. See [`Command Buffer Debugging`](command-buffer-debugging.md) for more methods and properties that can help you isolate the issue.

> ⚠️ **Warning**:  Avoid calling the [`insertDebugCaptureBoundary()`](mtlcommandqueue/insertdebugcaptureboundary().md) method within the completion handler, which can cause a debug-time deadlock if you request GPU frame capture.

## Parameters

- `block`: A Swift closure or an Objective-C block that Metal calls after the GPU finishes running the commands in the command buffer.

## See Also

- [func addScheduledHandler(MTLCommandBufferHandler)](mtlcommandbuffer/addscheduledhandler(_:).md)
  Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [typealias MTLCommandBufferHandler](mtlcommandbufferhandler.md)
  A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/addcompletedhandler(_:))*