# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An object the describes the error that caused the rendering failure.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- tvOS 17.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (readonly, nullable) NSError * error;
```

## Discussion

This value is `nil` by default. It only contains a valid error object when the [`status`](./status.md) value is [`AVQueuedSampleBufferRenderingStatus.failed`](../avqueuedsamplebufferrenderingstatus/failed.md).

## See Also

### Inspecting the status
- [var status: AVQueuedSampleBufferRenderingStatus](./status.md)
  A status value that indicates whether this object can enqueue and render sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/error)*