# AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The sample buffer was not enqueued because the Receiver failed.

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
case cancelledDueToError(any Error)
```

## See Also

### Enqueue results
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued](./enqueued.md)
  The sample buffer was enqueued successfully.
- [case enqueuedWithSuggestedFlush([AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason])](./enqueuedwithsuggestedflush%28_%29.md)
  The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](./cancelledduetoflush.md)
  The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror(_:))*