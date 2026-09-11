# AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued

**Framework**: AVFoundation  
**Kind**: case

The sample buffer was enqueued successfully.

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
case enqueued
```

## See Also

- [case enqueuedWithSuggestedFlush([AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason])](avsamplebufferaudiorenderer/receiver/enqueueresult/enqueuedwithsuggestedflush(_:).md)
  The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror(_:).md)
  The sample buffer was not enqueued because the Receiver failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/enqueued)*