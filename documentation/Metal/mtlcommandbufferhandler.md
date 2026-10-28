# MTLCommandBufferHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLCommandBufferHandler = @Sendable (any MTLCommandBuffer) -> Void
```

```c
typedef void (^)(id<MTLCommandBuffer>) MTLCommandBufferHandler;
```

## Discussion

The [`MTLCommandBuffer`](./mtlcommandbuffer.md) type uses this signature in its methods that register your completion handlers, including [`addScheduledHandler(_:)`](./mtlcommandbuffer/addscheduledhandler%28_%29.md) and [`addCompletedHandler(_:)`](./mtlcommandbuffer/addcompletedhandler%28_%29.md).

## Parameters

- `commandBuffer`: The [`MTLCommandBuffer`](./mtlcommandbuffer.md) instance that’s invoking the completion handler.

## See Also

### Registering state change handlers
- [func addScheduledHandler(MTLCommandBufferHandler)](./mtlcommandbuffer/addscheduledhandler%28_%29.md)
  Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [func addCompletedHandler(MTLCommandBufferHandler)](./mtlcommandbuffer/addcompletedhandler%28_%29.md)
  Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferhandler)*