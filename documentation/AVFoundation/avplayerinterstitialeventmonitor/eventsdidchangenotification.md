# eventsDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when the monitor’s schedule of interstitial events changes.

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
class let eventsDidChangeNotification: NSNotification.Name
```

## See Also

- [var events: [AVPlayerInterstitialEvent]](avplayerinterstitialeventmonitor/events.md)
  The schedule of interstitial events.
- [class let interstitialEventWasUnscheduledNotification: NSNotification.Name](avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification.md)
  A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.
- [class let interstitialEventWasUnscheduledEventKey: String](avplayerinterstitialeventmonitor/interstitialeventwasunscheduledeventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [class let interstitialEventWasUnscheduledErrorKey: String](avplayerinterstitialeventmonitor/interstitialeventwasunschedulederrorkey.md)
  The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [class let interstitialEventDidFinishNotification: NSNotification.Name](avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification.md)
  A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.
- [class let interstitialEventDidFinishEventKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinisheventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishPlayoutTimeKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinishplayouttimekey.md)
  The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishDidPlayEntireEventKey: String](avplayerinterstitialeventmonitor/interstitialeventdidfinishdidplayentireeventkey.md)
  The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/eventsdidchangenotification)*