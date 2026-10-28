# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.

**Availability**:
- iOS 14.5+ - Deprecated in 18.0
- iPadOS 14.5+ - Deprecated in 18.0
- Mac Catalyst 14.5+ - Deprecated in 18.0
- macOS 11.3+ - Deprecated in 15.0
- tvOS 14.5+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's hasSufficientMediaDataForReliablePlaybackStart instead

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasSufficientMediaDataForReliablePlaybackStart;
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`hasSufficientMediaDataForReliablePlaybackStart`](../avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

## See Also

### Initiating media data requests
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current media data request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart)*