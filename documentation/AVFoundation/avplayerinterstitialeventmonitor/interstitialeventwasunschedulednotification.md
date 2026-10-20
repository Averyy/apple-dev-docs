# interstitialEventWasUnscheduledNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.

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
class let interstitialEventWasUnscheduledNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification;
```

#### Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey, with a value that indicates which AVPlayerInterstitialEvent was unscheduled.
2. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey, with an NSError value. This key will only be present if the AVPlayerInterstitialEvent was unscheduled due to an error.

## See Also

### Monitoring the event schedule
- [var events: [AVPlayerInterstitialEvent]](./events.md)
  The schedule of interstitial events.
- [class let eventsDidChangeNotification: NSNotification.Name](./eventsdidchangenotification.md)
  A notification the system posts when the monitor’s schedule of interstitial events changes.
- [class let interstitialEventWasUnscheduledEventKey: String](./interstitialeventwasunscheduledeventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that was unscheduled in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification.
- [class let interstitialEventWasUnscheduledErrorKey: String](./interstitialeventwasunschedulederrorkey.md)
  The dictionary key to indicate whether the event that was unscheduled was due to an error.
- [class let interstitialEventDidFinishNotification: NSNotification.Name](./interstitialeventdidfinishnotification.md)
  A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.
- [class let interstitialEventDidFinishEventKey: String](./interstitialeventdidfinisheventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishPlayoutTimeKey: String](./interstitialeventdidfinishplayouttimekey.md)
  The dictionary key for the playout time of the event that finished playing in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.
- [class let interstitialEventDidFinishDidPlayEntireEventKey: String](./interstitialeventdidfinishdidplayentireeventkey.md)
  The dictionary key to indicate whether the event that finished playing was fully played out in the payload of the AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification)*