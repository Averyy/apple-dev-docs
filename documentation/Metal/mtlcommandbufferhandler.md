# MTLCommandBufferHandler

**Framework**: Metal  
**Kind**: typealias

A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLCommandBufferHandler = (any MTLCommandBuffer) -> Void
```

#### Discussion

The [`MTLCommandBuffer`](mtlcommandbuffer.md) type uses this signature in its methods that register your completion handlers, including [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) and [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md).

## Parameters

- `commandBuffer`: The   instance that’s invoking the completion handler.

## See Also

- [func addScheduledHandler(MTLCommandBufferHandler)](mtlcommandbuffer/addscheduledhandler(_:).md)
  Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [func addCompletedHandler(MTLCommandBufferHandler)](mtlcommandbuffer/addcompletedhandler(_:).md)
  Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferhandler)*