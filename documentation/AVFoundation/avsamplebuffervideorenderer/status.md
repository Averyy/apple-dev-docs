# status

**Framework**: AVFoundation  
**Kind**: property

A status value that indicates whether this object can enqueue and render sample buffers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

#### Discussion

If the status is [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md), check the value of the [`error`](avsamplebuffervideorenderer/error.md) property to determine the failure. To resume rendering sample buffers after a failure, you must first reset the status to [`AVQueuedSampleBufferRenderingStatus.unknown`](avqueuedsamplebufferrenderingstatus/unknown.md), which you do by invoking [`flush()`](avqueuedsamplebufferrendering/flush().md) on the video renderer.

This property is key-value observable.

## See Also

- [var error: (any Error)?](avsamplebuffervideorenderer/error.md)
  An object the describes the error that caused the rendering failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/status)*