# isReadyForMoreMediaData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the readiness of the layer to accept more sample buffers.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's readyForMoreMediaData instead

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

```objc
@property (readonly, getter=isReadyForMoreMediaData) BOOL readyForMoreMediaData;
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`isReadyForMoreMediaData`](../avqueuedsamplebufferrendering/isreadyformoremediadata.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

`AVSampleBufferDisplayLayer` keeps track of the occupancy levels of its internal queues for the benefit of clients that enqueue sample buffers from non-real-time sources — that is, clients that can supply sample buffers faster than they are consumed and need to decide when to hold back buffers.

Clients enqueueing sample buffers from non-real-time sources may hold off from generating or obtaining more sample buffers to enqueue when the value of `readyForMoreMediaData` is [`false`](../../Swift/false.md).

It is safe to call [`enqueue(_:)`](./enqueue%28_%29.md) when [`isReadyForMoreMediaData`](./isreadyformoremediadata.md) is [`false`](../../Swift/false.md), but enqueing more sample buffers than are required for timely rendering by the receiver is highly discouraged.

To help with control of the non-real-time supply of sample buffers, such clients should use [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) in order to specify a block that the layer should invoke whenever it’s ready for sample buffers to be appended.

The value of `readyForMoreMediaData` will often change from [`false`](../../Swift/false.md) to [`true`](../../Swift/true.md) asynchronously, as previously supplied sample buffers are decoded and displayed.

> ❗ **Important**:  This property does not support key-value observing.

## See Also

### Initiating media data requests
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](./hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/isreadyformoremediadata)*