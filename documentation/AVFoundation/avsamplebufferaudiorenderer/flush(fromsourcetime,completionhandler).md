# flush(fromSourceTime:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Flushes queued sample buffers with presentation time stamps later than or equal to the specified time.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush(fromSourceTime:) method instead

## Declaration

```swift
func flush(fromSourceTime time: CMTime, completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func flush(fromSourceTime time: CMTime) async -> Bool
```

```objc
- (void) flushFromSourceTime:(CMTime) time completionHandler:(void (^)(BOOL flushSucceeded)) completionHandler;
```

## Discussion

This method can be used to replace media data scheduled to be rendered in the future, without interrupting playback. One example of this is when the data that has already been enqueued is from a sequence of two songs and the second song is swapped for a new song. In this case, this method would be called with the timestamp of the first sample buffer from the second song. After the completion handler is executed with a `YES` parameter, media data may again be enqueued with time stamps at the specified time.

 If `NO` is provided to the completion handler, the flush did not succeed and the set of enqueued sample buffers remains unchanged. A flush can fail because the source time was too close to (or earlier than) the current time or because the current configuration of the receiver does not support flushing at a particular time. In these cases, the caller can choose to flush all enqueued media data by invoking [`flush()`](../avsamplebufferdisplaylayer/flush%28%29.md).

## Parameters

- `time`: The time used to flush all later sample buffers.
- `completionHandler`: The block to invoke when the flush operation has either been completed or been interrupted. The block takes one argument:

  - **flushSucceeded**: A Boolean value indicating whether the sample buffers were flushed.

## See Also

### Removing queued buffers
- [let AVSampleBufferAudioRendererFlushTimeKey: String](../avsamplebufferaudiorendererflushtimekey.md)
  The key that indicates the presentation timestamp of the first queued sample that was flushed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/flush(fromsourcetime:completionhandler:))*