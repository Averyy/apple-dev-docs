# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

## Declaration

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

```objc
- (void) requestMediaDataWhenReadyOnQueue:(dispatch_queue_t) queue usingBlock:(void (^)()) block;
```

#### Discussion

When this method is called multiple times, only the last call is implemented. Pair each call to [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) with a corresponding call to [`stopRequestingMediaData()`](./stoprequestingmediadata%28%29.md). Releasing the `AVQueuedSampleBufferRendering` object without a call to `stopRequestingMediaData` results in undefined behavior.

## Parameters

- `queue`: The dispatch queue.
- `block`: A block that enqueues sample buffers until the receiver is no longer ready or there is no more data to supply.

## See Also

### Requesting media
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func enqueue(CMSampleBuffer)](./enqueue%28_%29.md)
  Sends a sample buffer to the queue for rendering.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:))*