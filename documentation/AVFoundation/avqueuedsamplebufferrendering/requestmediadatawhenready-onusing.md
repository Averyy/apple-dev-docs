# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.

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
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping () -> Void)
```

#### Discussion

When this method is called multiple times, only the last call is implemented. Pair each call to [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) with a corresponding call to [`stopRequestingMediaData()`](avqueuedsamplebufferrendering/stoprequestingmediadata().md). Releasing the `AVQueuedSampleBufferRendering` object without a call to `stopRequestingMediaData` results in undefined behavior.

## Parameters

- `queue`: The dispatch queue.
- `block`: A block that enqueues sample buffers until the receiver is no longer ready or there is no more data to supply.

## See Also

- [var isReadyForMoreMediaData: Bool](avqueuedsamplebufferrendering/isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func enqueue(CMSampleBuffer)](avqueuedsamplebufferrendering/enqueue(_:).md)
  Sends a sample buffer to the queue for rendering.
- [func stopRequestingMediaData()](avqueuedsamplebufferrendering/stoprequestingmediadata.md)
  Cancels any current [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:))*