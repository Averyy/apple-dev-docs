# AVSampleBufferRenderSynchronizer

**Framework**: AVFoundation  
**Kind**: class

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

## Mentions

- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)
- [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md)

#### Overview

This class synchronizes multiple objects that conform to [`AVQueuedSampleBufferRendering`](avqueuedsamplebufferrendering.md) to a single timeline.

## Topics

### Managing Renderers
- [var renderers: [any AVQueuedSampleBufferRendering]](avsamplebufferrendersynchronizer/renderers.md)
  An array of queued sample buffer renderers currently attached to the synchronizer.
- [func addRenderer(any AVQueuedSampleBufferRendering)](avsamplebufferrendersynchronizer/addrenderer(_:).md)
  Adds a renderer to the list of renderers under the synchronizer’s control.
- [func removeRenderer(any AVQueuedSampleBufferRendering, at: CMTime, completionHandler: ((Bool) -> Void)?)](avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:).md)
  Removes a renderer from the synchronizer.
### Accessing Time Information
- [func currentTime() -> CMTime](avsamplebufferrendersynchronizer/currenttime.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](avsamplebufferrendersynchronizer/timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](avsamplebufferrendersynchronizer/rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:).md)
  Sets the renderer’s time and rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:athosttime:).md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](avsamplebufferrendersynchronizer/ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.
### Observing Time
- [func addPeriodicTimeObserver(forInterval: CMTime, queue: dispatch_queue_t?, using: (CMTime) -> Void) -> Any](avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval:queue:using:).md)
  Requests invocation of a block during rendering at specified time intervals.
- [func addBoundaryTimeObserver(forTimes: [NSValue], queue: dispatch_queue_t?, using: () -> Void) -> Any](avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes:queue:using:).md)
  Requests invocation of a block when specified times are traversed during normal rendering.
- [func removeTimeObserver(Any)](avsamplebufferrendersynchronizer/removetimeobserver(_:).md)
  Cancels the specified time observer.
### Instance Properties
- [var intendedSpatialAudioExperience: any SpatialAudioExperience](avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3.md)
  The intended spatial audio experience applied to all `AVSampleBufferAudioRenderer`’s within this synchronizer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
  Methods you can implement to enqueue sample buffers for presentation.
- [class AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md)
  An object that displays compressed or uncompressed video frames.
- [class AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.
- [class AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer)*