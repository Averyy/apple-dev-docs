# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`hasSufficientMediaDataForReliablePlaybackStart`](avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

## See Also

- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](avsamplebufferdisplaylayer/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](avsamplebufferdisplaylayer/stoprequestingmediadata.md)
  Cancels any current media data request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart)*