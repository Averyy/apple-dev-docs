# stopRequestingMediaData()

**Framework**: AVFoundation  
**Kind**: method

Cancels any current media data request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func stopRequestingMediaData()
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`stopRequestingMediaData()`](avqueuedsamplebufferrendering/stoprequestingmediadata().md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

This method cancels any current [`requestMediaDataWhenReady(on:using:)`](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md) call. Each invocation of [`requestMediaDataWhenReady(on:using:)`](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md) must be balanced by a call to this method.

This method may be called from within the [`requestMediaDataWhenReady(on:using:)`](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md) method’s block or from outside the block.

## See Also

- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](avsamplebufferdisplaylayer/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/stoprequestingmediadata())*