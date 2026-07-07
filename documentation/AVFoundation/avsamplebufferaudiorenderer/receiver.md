# AVSampleBufferAudioRenderer.Receiver

**Framework**: AVFoundation  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
class Receiver
```

## Topics

### Enqueuing sample buffers
- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueueimmediately(_:).md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.
### Flushing the receiver
- [func flush()](avsamplebufferaudiorenderer/receiver/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func flush(fromSourceTime: CMTime) async -> Bool](avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:).md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason](avsamplebufferaudiorenderer/receiver/suggestedflushreason.md)
  Reasons the receiver suggests the client flush and re-enqueue.
### Observing rendering events
- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferAudioRenderer.Receiver.RenderingEvent, Never>](avsamplebufferaudiorenderer/receiver/renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent](avsamplebufferaudiorenderer/receiver/renderingevent.md)
  Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver)*