# requiresFlushToResumeDecoding

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's requiresFlushToResumeDecoding instead

## Declaration

```swift
var requiresFlushToResumeDecoding: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL requiresFlushToResumeDecoding;
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`requiresFlushToResumeDecoding`](../avsamplebuffervideorenderer/requiresflushtoresumedecoding.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

When an app enters a state where use of video decoder resources isn’t permissible, the value of this property changes to [`true`](../../Swift/true.md) and the display layer’s status changes to a [`AVQueuedSampleBufferRenderingStatus.failed`](../avqueuedsamplebufferrenderingstatus/failed.md) state.

To resume rendering sample buffers using the display layer after this property’s value is [`true`](../../Swift/true.md), apps must first reset the display layer’s status to [`AVQueuedSampleBufferRenderingStatus.unknown`](../avqueuedsamplebufferrenderingstatus/unknown.md), which you do by calling the layer’s [`flush()`](./flush%28%29.md) method.

This property isn’t key-value observable. Instead, observe changes to this property value by observing notifications of type [`AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification`](../avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.md).

## See Also

### Initiating media data requests
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](./hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requiresflushtoresumedecoding)*