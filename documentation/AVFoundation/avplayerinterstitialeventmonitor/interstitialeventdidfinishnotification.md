# interstitialEventDidFinishNotification

**Framework**: AVFoundation  
**Kind**: property

A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class let interstitialEventDidFinishNotification: NSNotification.Name
```

#### Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey, with a value that indicates the AVPlayerInterstitialEvent that finished playing.
2. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey, with a value that indicates how long that AVPlayerInterstitialEvent played out for.
3. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey, with a value that indicates whether the AVPlayerInterstitialEvent was fully played out.

Note that cancelling an AVPlayerInterstitialEvent after playback started but prior to playback finishing will also trigger this event.

## See Also

- [var events: [AVPlayerInterstitialEvent]](avplayerinterstitialeventmonitor/events.md)
  The schedule of interstitial events.
- [class let eventsDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/eventsdidchangenotification.md)
  A notification the system posts when the monitor’s schedule of interstitial events changes.
- [class let interstitialEventWasUnscheduledNotification: NSNotification.Name](avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification.md)
  A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.
- [class let interstitialEventWasUnscheduledEventKey: String](avplayerinterstitialeventmonitor/interstitialeventwasunscheduledeventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [class let interstitialEventWasUnscheduledErrorKey: String](avplayerinterstitialeventmonitor/interstitialeventwasunschedulederrorkey.md)
  The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [class let interstitialEventDidFinishEventKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinisheventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishPlayoutTimeKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinishplayouttimekey.md)
  The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishDidPlayEntireEventKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinishdidplayentireeventkey.md)
  The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification)*