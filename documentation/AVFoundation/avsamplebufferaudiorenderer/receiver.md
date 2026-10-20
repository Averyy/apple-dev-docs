# AVSampleBufferAudioRenderer.Receiver

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class Receiver
```

## Topics

### Enqueuing sample buffers
- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](./receiver/enqueue%28_%29.md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](./receiver/enqueueimmediately%28_%29.md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult](./receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.
### Flushing the receiver
- [func flush()](./receiver/flush%28%29.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func flush(fromSourceTime: CMTime) async -> Bool](./receiver/flush%28fromsourcetime%29.md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason](./receiver/suggestedflushreason.md)
  Reasons the receiver suggests the client flush and re-enqueue.
### Observing rendering events
- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferAudioRenderer.Receiver.RenderingEvent, Never>](./receiver/renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent](./receiver/renderingevent.md)
  Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver)*