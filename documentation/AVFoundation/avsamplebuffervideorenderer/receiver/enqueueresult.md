# AVSampleBufferVideoRenderer.Receiver.EnqueueResult

**Framework**: AVFoundation  
**Kind**: enum

A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum EnqueueResult
```

## Topics

### Enqueue results
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](avsamplebuffervideorenderer/receiver/enqueueresult/enqueued.md)
  The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)](avsamplebuffervideorenderer/receiver/enqueueresult/enqueuedwithdecodefailures(_:).md)
  The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush](avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflushrequiredtoresume(_:).md)
  The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoerror(_:).md)
  The sample buffer was not enqueued because the Receiver failed.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueimmediately(_:).md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult)*