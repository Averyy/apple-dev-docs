# addScheduledHandler(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func addScheduledHandler(_ block: @escaping MTLCommandBufferHandler)
```

## Mentions

- [Setting up a command structure](setting-up-a-command-structure.md)

#### Discussion

You can register one or more scheduling completion handlers for the same command buffer. The GPU device’s driver (on the CPU) calls the completion handlers after it finishes scheduling the command buffer to run on the GPU.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

The GPU device schedules each command buffer — along with tasks from other command buffers — after it identifies the command buffer’s dependencies. At that time, the GPU device sets the command buffer’s status to [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md) and calls your completion handler.

> **Note**:  The command buffer’s [`status`](mtlcommandbuffer/status.md) property may be equal to another (larger) value by the time your completion handler runs, including [`MTLCommandBufferStatus.completed`](mtlcommandbufferstatus/completed.md).

You can use the command buffer’s [`kernelEndTime`](mtlcommandbuffer/kernelendtime.md) and [`kernelStartTime`](mtlcommandbuffer/kernelstarttime.md) properties to calculate how much time the CPU spends scheduling the command buffer.

## Parameters

- `block`: A Swift closure or an Objective-C block that Metal calls after it schedules the command buffer to run on the GPU.

## See Also

- [func addCompletedHandler(MTLCommandBufferHandler)](mtlcommandbuffer/addcompletedhandler(_:).md)
  Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.
- [typealias MTLCommandBufferHandler](mtlcommandbufferhandler.md)
  A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/addscheduledhandler(_:))*