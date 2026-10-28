# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's requestMediaDataWhenReadyOnQueue:usingBlock: instead

## Declaration

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

```objc
- (void) requestMediaDataWhenReadyOnQueue:(dispatch_queue_t) queue usingBlock:(void (^)()) block;
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`requestMediaDataWhenReady(on:using:)`](../avqueuedsamplebufferrendering/requestmediadatawhenready%28on,using%29.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

The block is expected to call the [`enqueue(_:)`](./enqueue%28_%29.md) in order to provide media data for decompression (if necessary) and rendering while the [`isReadyForMoreMediaData`](./isreadyformoremediadata.md) property remains [`true`](../../Swift/true.md), or until it can provide no additional media. When the layer has decoded enough media data that it is ready for additional media data, it will invoke the block again.

By allowing the display layer to determine when to invoke the block, the implementation of incremental I/O operations is simplified when supplying synchronized media data during rendering.

If this function is called multiple times, only the last call is effective.

You invoke the [`stopRequestingMediaData()`](./stoprequestingmediadata%28%29.md) method to cancel this request.

Each call to `requestMediaDataWhenReadyOnQueue:usingBlock:` must be balanced with a corresponding call to [`stopRequestingMediaData()`](./stoprequestingmediadata%28%29.md).

Releasing the receiver instance without a call to [`stopRequestingMediaData()`](./stoprequestingmediadata%28%29.md) will result in undefined behavior.

## Parameters

- `queue`: The dispatch queue.
- `block`: The block that provides media data.

## See Also

### Initiating media data requests
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](./hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:))*