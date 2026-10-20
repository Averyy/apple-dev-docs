# stopRequestingMediaData()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels any current media data request.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's stopRequestingMediaData instead

## Declaration

```swift
func stopRequestingMediaData()
```

```objc
- (void) stopRequestingMediaData;
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`stopRequestingMediaData()`](../avqueuedsamplebufferrendering/stoprequestingmediadata%28%29.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

This method cancels any current [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) call. Each invocation of [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) must be balanced by a call to this method.

This method may be called from within the [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) method’s block or from outside the block.

## See Also

### Initiating media data requests
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](./hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/stoprequestingmediadata())*