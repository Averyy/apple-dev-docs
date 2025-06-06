# AVPlayerInterstitialEventMonitor

**Framework**: AVFoundation  
**Kind**: class

An object that monitors the scheduling and progress of interstitial events.

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
class AVPlayerInterstitialEventMonitor
```

#### Overview

This object monitors interstitial events that exist within the content of the primary items, such as events defined by an HLS media playlist, and also events managed by an [`AVPlayerInterstitialEventController`](avplayerinterstitialeventcontroller.md) object. You can access the schedule of interstitial events through the [`events`](avplayerinterstitialeventmonitor/events.md) property.

When it’s time to present an interstitial event, the system suspends playback of the primary item and changes its player’s [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) to [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) with a [`reasonForWaitingToPlay`](avplayer/reasonforwaitingtoplay.md) value of [`interstitialEvent`](avplayer/waitingreason/interstitialevent.md). When the system suspends primary playback, it creates player items based on the event’s [`templateItems`](avplayerinterstitialevent/templateitems.md) to play interstitial content. The interstitial player temporarily assumes the primary player’s output configuration, such as routing its visual output to player layers that reference the primary player. After the interstitial player finishes playback, or its current item otherwise becomes `nil`, playback of primary content resumes.

## Topics

### Creating a monitor
- [init(primaryPlayer: AVPlayer)](avplayerinterstitialeventmonitor/init(primaryplayer:).md)
  Creates an observer with a player item.
### Monitoring the current event
- [var currentEvent: AVPlayerInterstitialEvent?](avplayerinterstitialeventmonitor/currentevent.md)
  The current interstitial event.
- [class let currentEventDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/currenteventdidchangenotification.md)
  A notification the system posts when the monitor’s current interstitial event changes.
### Monitoring the event schedule
- [var events: [AVPlayerInterstitialEvent]](avplayerinterstitialeventmonitor/events.md)
  The schedule of interstitial events.
- [class let eventsDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/eventsdidchangenotification.md)
  A notification the system posts when the monitor’s schedule of interstitial events changes.
### Monitoring the asset list response
- [class let assetListResponseStatusDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md)
  A notification the system posts when the status of an interstitial event’s asset list response changes.
- [enum AVPlayerInterstitialEventAssetListResponseStatus](avplayerinterstitialeventassetlistresponsestatus.md)
  Constants that describe the status of the asset list response for an interstitial event.
### Accessing the players
- [var primaryPlayer: AVPlayer?](avplayerinterstitialeventmonitor/primaryplayer.md)
  An object that plays primary content.
- [var interstitialPlayer: AVQueuePlayer](avplayerinterstitialeventmonitor/interstitialplayer.md)
  An object that plays interstitial content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Providing an integrated view of your timeline when playing HLS interstitials](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md)
  Go beyond simple ad insertion with point and fill occupancy HLS interstitials.
- [class AVPlayerInterstitialEvent](avplayerinterstitialevent.md)
  An object that provides instructions for how a player presents interstitial content.
- [class AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md)
  An object that schedules interstitial events for items played by the primary player.
- [class AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md)
  An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor)*