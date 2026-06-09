# flush(fromSourceTime:)

**Framework**: AVFoundation  
**Kind**: method

Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.

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
nonisolated
(nonsending) func flush(fromSourceTime sourceTime: CMTime) async -> Bool
```

#### Return Value

If the flush was successful, this method returns `true`. Otherwise it returns `false`.

#### Discussion

This method can be used to replace media data scheduled to be rendered in the future, without interrupting playback.  One example of this is when the data that has already been enqueued is from a sequence of two songs and the second song is swapped for a new song.  In this case, this method would be called with the time stamp of the first sample buffer from the second song.  After this method resumes returning `true`, media data may again be enqueued with timestamps at the specified time.

If this method returns `false`, the flush did not succeed and the set of enqueued sample buffers remains unchanged.  A flush can fail because the source time was too close to (or earlier than) the current time or because the current configuration of the receiver does not support flushing at a particular time.  In these cases, the caller can choose to flush all enqueued media data by invoking the `flush()` method.

## Parameters

- `sourceTime`: The source time for the flush to take effect.

## See Also

- [func flush()](avsamplebufferaudiorenderer/receiver/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason](avsamplebufferaudiorenderer/receiver/suggestedflushreason.md)
  Reasons the receiver suggests the client flush and re-enqueue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:))*