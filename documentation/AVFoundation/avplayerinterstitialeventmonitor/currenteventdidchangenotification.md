# currentEventDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification the system posts when the monitor’s current interstitial event changes.

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
class let currentEventDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVPlayerInterstitialEventMonitorCurrentEventDidChangeNotification;
```

## See Also

### Monitoring the current event
- [var currentEvent: AVPlayerInterstitialEvent?](./currentevent.md)
  The current interstitial event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventdidchangenotification)*