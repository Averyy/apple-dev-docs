# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method

Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping () -> Void)
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

The block is expected to call the [`enqueue(_:)`](avsamplebufferdisplaylayer/enqueue(_:).md) in order to provide media data for decompression (if necessary) and rendering while the [`isReadyForMoreMediaData`](avsamplebufferdisplaylayer/isreadyformoremediadata.md) property remains [`true`](https://developer.apple.com/documentation/Swift/true), or until it can provide no additional media. When the layer has decoded enough media data that it is ready for additional media data, it will invoke the block again.

By allowing the display layer to determine when to invoke the block, the implementation of incremental I/O operations is simplified when supplying synchronized media data during rendering.

If this function is called multiple times, only the last call is effective.

You invoke the [`stopRequestingMediaData()`](avsamplebufferdisplaylayer/stoprequestingmediadata().md) method to cancel this request.

Each call to `requestMediaDataWhenReadyOnQueue:usingBlock:` must be balanced with a corresponding call to [`stopRequestingMediaData()`](avsamplebufferdisplaylayer/stoprequestingmediadata().md).

Releasing the receiver instance without a call to [`stopRequestingMediaData()`](avsamplebufferdisplaylayer/stoprequestingmediadata().md) will result in undefined behavior.

## Parameters

- `queue`: The dispatch queue.
- `block`: The block that provides media data.

## See Also

- [var isReadyForMoreMediaData: Bool](avsamplebufferdisplaylayer/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](avsamplebufferdisplaylayer/stoprequestingmediadata.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:))*