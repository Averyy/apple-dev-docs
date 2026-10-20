# AVQueuedSampleBufferRendering

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to enqueue sample buffers for presentation.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use an AVSampleBufferVideoRenderer or AVSampleBufferAudioRenderer with a render synchronizer instead

## Declaration

```swift
protocol AVQueuedSampleBufferRendering : NSObjectProtocol
```

```objc
@protocol AVQueuedSampleBufferRendering <NSObject>
```

#### Overview

[`AVSampleBufferDisplayLayer`](./avsamplebufferdisplaylayer.md) and [`AVSampleBufferAudioRenderer`](./avsamplebufferaudiorenderer.md) conform to this protocol. When used in conjunction with an [`AVSampleBufferRenderSynchronizer`](./avsamplebufferrendersynchronizer.md), an object conforming to `AVQueuedSampleBufferRendering` can only be attached to a single synchronizer.

## Topics

### Requesting media
- [var isReadyForMoreMediaData: Bool](./avqueuedsamplebufferrendering/isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func enqueue(CMSampleBuffer)](./avqueuedsamplebufferrendering/enqueue%28_%29.md)
  Sends a sample buffer to the queue for rendering.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./avqueuedsamplebufferrendering/requestmediadatawhenready%28on,using%29.md)
  Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.
- [func stopRequestingMediaData()](./avqueuedsamplebufferrendering/stoprequestingmediadata%28%29.md)
  Cancels any current [`requestMediaDataWhenReady(on:using:)`](./avqueuedsamplebufferrendering/requestmediadatawhenready%28on,using%29.md) call.
### Determining playback readiness
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](./avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqued media meets the required preroll level for reliable playback.
### Clearing queued sample buffers
- [func flush()](./avqueuedsamplebufferrendering/flush%28%29.md)
  Discards all pending enqueued sample buffers.
### Indentifying the timebase
- [var timebase: CMTimebase](./avqueuedsamplebufferrendering/timebase.md)
  The timebase for a renderer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [AVSampleBufferAudioRenderer](./avsamplebufferaudiorenderer.md)
- [AVSampleBufferDisplayLayer](./avsamplebufferdisplaylayer.md)
- [AVSampleBufferVideoRenderer](./avsamplebuffervideorenderer.md)

## See Also

### Presentation
- [class AVSampleBufferRenderSynchronizer](./avsamplebufferrendersynchronizer.md)
  An object used to synchronize multiple queued sample buffers to a single timeline.
- [class AVSampleBufferDisplayLayer](./avsamplebufferdisplaylayer.md)
  An object that displays compressed or uncompressed video frames.
- [class AVSampleBufferVideoRenderer](./avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.
- [class AVSampleBufferAudioRenderer](./avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering)*