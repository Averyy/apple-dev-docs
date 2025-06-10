# AVPlayerItemIntegratedTimeline

**Framework**: AVFoundation  
**Kind**: class

An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class AVPlayerItemIntegratedTimeline
```

#### Overview

The timeline models all regions to traverse during playback. A player may not present portions of the primary item when exiting an interstitial event with a positive resumption offset.

## Topics

### Inspecting snapshots
- [var currentSnapshot: AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimeline/currentsnapshot.md)
  An immutable representation of the timeline state at time of request.
- [class AVPlayerItemIntegratedTimelineSnapshot](avplayeritemintegratedtimelinesnapshot.md)
  An immutable representation of inspectable details of an integrated timeline object.
- [class let snapshotsOutOfSyncNotification: NSNotification.Name](avplayeritemintegratedtimeline/snapshotsoutofsyncnotification.md)
  A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.
### Inspecting the time and date
- [var currentTime: CMTime](avplayeritemintegratedtimeline/currenttime.md)
  The current time on the integrated timeline.
- [var currentDate: Date?](avplayeritemintegratedtimeline/currentdate.md)
  The current date of playback.
### Seeking
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritemintegratedtimeline/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Seeks to a particular time in the integrated time domain.
- [func seek(to: Date, completionHandler: ((Bool) -> Void)?)](avplayeritemintegratedtimeline/seek(to:completionhandler:).md)
  Seeks to a particular date in the integrated time domain.
### Observing time changes
- [func periodicTimes(forInterval: CMTime) -> AVPlayerItemIntegratedTimeline.PeriodicTimes](avplayeritemintegratedtimeline/periodictimes(forinterval:).md)
  Returns an asynchronous sequence of times periodically as playback progresses.
- [func boundaryTimes(for: AVPlayerItemSegment, offsetsIntoSegment: [CMTime]) -> AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes(for:offsetsintosegment:).md)
  Returns an asynchronous sequence of times whenever playback reaches a segment time in the segment.
- [AVPlayerItemIntegratedTimeline.BoundaryTimes](avplayeritemintegratedtimeline/boundarytimes.md)
  An asynchronous sequence of boundary time values.
- [AVPlayerItemIntegratedTimeline.PeriodicTimes](avplayeritemintegratedtimeline/periodictimes.md)
  An asynchronous sequence of periodic time values.
- [protocol AVPlayerItemIntegratedTimelineObserver](avplayeritemintegratedtimelineobserver.md)
  A protocol for objects that perform timeline observations.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md)
  Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [class AVPlayerInterstitialEvent](avplayerinterstitialevent.md)
  An object that provides instructions for how a player presents interstitial content.
- [class AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md)
  An object that schedules interstitial events for items played by the primary player.
- [class AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)
  An object that monitors the scheduling and progress of interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline)*