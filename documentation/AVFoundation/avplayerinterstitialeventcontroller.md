# AVPlayerInterstitialEventController

**Framework**: AVFoundation  
**Kind**: class

An object that schedules interstitial events for items played by the primary player.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AVPlayerInterstitialEventController
```

#### Overview

This class is a subclass of [`AVPlayerInterstitialEventMonitor`](avplayerinterstitialeventmonitor.md) that you use to manage the schedule of interstitial events to present during playback of primary content.

> ❗ **Important**:  Creating an event controller and setting a schedule causes playback to ignore interstitial events present in the source media.

## Topics

### Creating an event controller
- [init(primaryPlayer: AVPlayer)](avplayerinterstitialeventcontroller/init(primaryplayer:).md)
  Creates an event controller with a player item.
### Configuring the event schedule
- [var events: [AVPlayerInterstitialEvent]!](avplayerinterstitialeventcontroller/events.md)
  The current schedule of interstitial events.
- [func cancelCurrentEvent(withResumptionOffset: CMTime)](avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset:).md)
  Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.
- [func skipCurrentEvent()](avplayerinterstitialeventcontroller/skipcurrentevent.md)
  Causes the playback of the currently playing interstital event to be abandoned.
### Accessing strings
- [var localizedStringsBundle: Bundle?](avplayerinterstitialeventcontroller/localizedstringsbundle.md)
  The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.
- [var localizedStringsTableName: String?](avplayerinterstitialeventcontroller/localizedstringstablename.md)
  The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

## Relationships

### Inherits From
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)
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
- [class AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)
  An object that monitors the scheduling and progress of interstitial events.
- [class AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md)
  An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller)*