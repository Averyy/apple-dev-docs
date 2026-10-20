# AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case enqueuedWithDecodeFailures([any Error])
```

## See Also

### Enqueue results
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](./enqueued.md)
  The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush](./cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](./cancelledduetoflushrequiredtoresume%28_%29.md)
  The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](./cancelledduetoerror%28_%29.md)
  The sample buffer was not enqueued because the Receiver failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult/enqueuedwithdecodefailures(_:))*