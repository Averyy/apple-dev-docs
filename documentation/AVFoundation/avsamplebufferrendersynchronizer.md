# AVSampleBufferRenderSynchronizer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object used to synchronize multiple queued sample buffers to a single timeline.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class AVSampleBufferRenderSynchronizer
```

```objc
@interface AVSampleBufferRenderSynchronizer : NSObject
```

## Mentions

- [Implementing flexible enhanced buffering for your content](./implementing-flexible-enhanced-buffering-for-your-content.md)
- [Supporting AirPlay in your app](./supporting-airplay-in-your-app.md)

## Overview

This class synchronizes multiple objects that conform to [`AVQueuedSampleBufferRendering`](./avqueuedsamplebufferrendering.md) to a single timeline.

## Topics

### Managing renderers
- [var renderers: [any AVQueuedSampleBufferRendering]](./avsamplebufferrendersynchronizer/renderers.md)
  An array of queued sample buffer renderers currently attached to the synchronizer.
- [func addRenderer(any AVQueuedSampleBufferRendering)](./avsamplebufferrendersynchronizer/addrenderer%28_%29.md)
  Adds a renderer to the list of renderers under the synchronizer’s control.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](./avsamplebufferrendersynchronizer/removerenderer%28_,at,completionhandler%29.md)
  Removes a renderer from the synchronizer.
### Accessing time information
- [func currentTime() -> CMTime](./avsamplebufferrendersynchronizer/currenttime%28%29.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](./avsamplebufferrendersynchronizer/timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](./avsamplebufferrendersynchronizer/rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](./avsamplebufferrendersynchronizer/setrate%28_,time%29.md)
  Sets the renderer’s time and rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./avsamplebufferrendersynchronizer/setrate%28_,time,athosttime%29.md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](./avsamplebufferrendersynchronizer/ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](./avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.
### Observing time
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](./avsamplebufferrendersynchronizer/addperiodictimeobserver%28forinterval,queue,using%29.md)
  Requests invocation of a block during rendering at specified time intervals.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](./avsamplebufferrendersynchronizer/addboundarytimeobserver%28fortimes,queue,using%29.md)
  Requests invocation of a block when specified times are traversed during normal rendering.
- [func removeTimeObserver(Any)](./avsamplebufferrendersynchronizer/removetimeobserver%28_%29.md)
  Cancels the specified time observer.
### Configuring audio behavior
- [var intendedSpatialAudioExperience: any SpatialAudioExperience](./avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3.md)
  The synchronizer’s intended Spatial Audio experience.
- [intendedSpatialAudioExperience](./avsamplebufferrendersynchronizer/intendedspatialaudioexperience-2wthu.md)
  The intended spatial audio experience applied to all AVSampleBufferAudioRenderers within this synchronizer.
### Instance Methods
- [func removeReceiver(sending AVSampleBufferAudioRenderer.Receiver, at: CMTime) async -> Bool](./avsamplebufferrendersynchronizer/removereceiver%28_,at%29-3rrnp.md)
  Removes a receiver and its renderer from the synchronizer.
- [func removeReceiver(sending AVSampleBufferVideoRenderer.Receiver, at: CMTime) async -> Bool](./avsamplebufferrendersynchronizer/removereceiver%28_,at%29-3yxub.md)
  Removes a receiver and its renderer from the synchronizer.
- [func sampleBufferReceiver(adding: AVSampleBufferAudioRenderer) -> sending AVSampleBufferAudioRenderer.Receiver](./avsamplebufferrendersynchronizer/samplebufferreceiver%28adding%29-5dw84.md)
  Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.
- [func sampleBufferReceiver(adding: AVSampleBufferVideoRenderer) -> sending AVSampleBufferVideoRenderer.Receiver](./avsamplebufferrendersynchronizer/samplebufferreceiver%28adding%29-rxap.md)
  Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Presentation
- [protocol AVQueuedSampleBufferRendering](./avqueuedsamplebufferrendering.md)
  Methods you can implement to enqueue sample buffers for presentation.
- [class AVSampleBufferDisplayLayer](./avsamplebufferdisplaylayer.md)
  An object that displays compressed or uncompressed video frames.
- [class AVSampleBufferVideoRenderer](./avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.
- [class AVSampleBufferAudioRenderer](./avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer)*