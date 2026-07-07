# AVSampleBufferVideoRenderer.Receiver

**Framework**: AVFoundation  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class Receiver
```

## Topics

### Enqueuing sample buffers
- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueimmediately(_:).md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.
### Flushing the receiver
- [func flush()](avsamplebuffervideorenderer/receiver/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func flush(removingDisplayedImage: Bool) async](avsamplebuffervideorenderer/receiver/flush(removingdisplayedimage:).md)
  Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.
### Observing rendering events
- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferVideoRenderer.Receiver.RenderingEvent, Never>](avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent](avsamplebuffervideorenderer/receiver/renderingevent.md)
  Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver)*