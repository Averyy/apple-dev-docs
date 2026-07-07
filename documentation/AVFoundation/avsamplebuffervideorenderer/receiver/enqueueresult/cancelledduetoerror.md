# AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)

**Framework**: AVFoundation  
**Kind**: case

The sample buffer was not enqueued because the Receiver failed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case cancelledDueToError(any Error)
```

## See Also

- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](avsamplebuffervideorenderer/receiver/enqueueresult/enqueued.md)
  The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)](avsamplebuffervideorenderer/receiver/enqueueresult/enqueuedwithdecodefailures(_:).md)
  The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush](avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflushrequiredtoresume(_:).md)
  The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoerror(_:))*