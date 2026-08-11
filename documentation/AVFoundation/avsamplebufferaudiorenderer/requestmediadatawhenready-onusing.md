# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method

Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for playback.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

#### Discussion

The block should enqueue sample buffers to the receiver either until the receiver’s readyForMoreMediaData property becomes NO or until there is no more data to supply. When the receiver has decoded enough of the media data it has received that it becomes ready for more media data again, it will invoke the block again in order to obtain more.

If this method is called multiple times, only the last call is effective. Call stopRequestingMediaData to cancel this request.

Each call to requestMediaDataWhenReadyOnQueue:usingBlock: should be paired with a corresponding call to stopRequestingMediaData:. Releasing the AVQueuedSampleBufferRendering object without a call to stopRequestingMediaData will result in undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/requestmediadatawhenready(on:using:))*