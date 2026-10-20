# AVSampleBufferVideoRenderer.Receiver.EnqueueResult

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum EnqueueResult
```

## Topics

### Enqueue results
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](./enqueueresult/enqueued.md)
  The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)](./enqueueresult/enqueuedwithdecodefailures%28_%29.md)
  The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush](./enqueueresult/cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](./enqueueresult/cancelledduetoflushrequiredtoresume%28_%29.md)
  The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](./enqueueresult/cancelledduetoerror%28_%29.md)
  The sample buffer was not enqueued because the Receiver failed.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Enqueuing sample buffers
- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](./enqueue%28_%29.md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](./enqueueimmediately%28_%29.md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult)*