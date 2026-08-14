# requiresFlushToResumeDecoding

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var requiresFlushToResumeDecoding: Bool { get }
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`requiresFlushToResumeDecoding`](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

When an app enters a state where use of video decoder resources isn’t permissible, the value of this property changes to [`true`](https://developer.apple.com/documentation/swift/true) and the display layer’s status changes to a [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md) state.

To resume rendering sample buffers using the display layer after this property’s value is [`true`](https://developer.apple.com/documentation/swift/true), apps must first reset the display layer’s status to [`AVQueuedSampleBufferRenderingStatus.unknown`](avqueuedsamplebufferrenderingstatus/unknown.md), which you do by calling the layer’s [`flush()`](avsamplebufferdisplaylayer/flush().md) method.

This property isn’t key-value observable. Instead, observe changes to this property value by observing notifications of type [`AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification`](avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.md).

## See Also

- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](avsamplebufferdisplaylayer/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [func stopRequestingMediaData()](avsamplebufferdisplaylayer/stoprequestingmediadata.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requiresflushtoresumedecoding)*