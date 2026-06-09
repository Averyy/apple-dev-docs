# AVSampleBufferAudioRenderer.Receiver.EnqueueResult

**Framework**: AVFoundation  
**Kind**: enum

A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum EnqueueResult
```

## Topics

### Enqueue results
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued](avsamplebufferaudiorenderer/receiver/enqueueresult/enqueued.md)
  The sample buffer was enqueued successfully.
- [case enqueuedWithSuggestedFlush([AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason])](avsamplebufferaudiorenderer/receiver/enqueueresult/enqueuedwithsuggestedflush(_:).md)
  The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror(_:).md)
  The sample buffer was not enqueued because the Receiver failed.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueueimmediately(_:).md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult)*