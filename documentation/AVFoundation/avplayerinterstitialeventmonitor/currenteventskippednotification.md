# currentEventSkippedNotification

**Framework**: AVFoundation  
**Kind**: property

A notification that’s posted whenever an event was skipped via skip control.

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
class let currentEventSkippedNotification: NSNotification.Name
```

## See Also

- [class let currentEventSkippableStateDidChangeNotification: NSNotification.Name](avplayerinterstitialeventmonitor/currenteventskippablestatedidchangenotification.md)
  A notification that’s posted whenever the currentEventSkippableState of an AVPlayerInterstitialEventMonitor changes.
- [class let currentEventSkippableStateDidChangeEventKey: String](avplayerinterstitialeventmonitor/currenteventskippablestatedidchangeeventkey.md)
  The dictionary key for the AVPlayerInterstitial event that had its skippable event state changed in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippableStateDidChangeStateKey: String](avplayerinterstitialeventmonitor/currenteventskippablestatedidchangestatekey.md)
  The dictionary key for the skippable event state in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippableStateDidChangeSkipControlLabelKey: String](avplayerinterstitialeventmonitor/currenteventskippablestatedidchangeskipcontrollabelkey.md)
  The dictionary key for the skip label of the event in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippedEventKey: String](avplayerinterstitialeventmonitor/currenteventskippedeventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that was skipped in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification.
- [var currentEventSkipControlLabel: String?](avplayerinterstitialeventmonitor/currenteventskipcontrollabel.md)
  The skip control label for the currentEvent.
- [var currentEventSkippableState: AVPlayerInterstitialEvent.SkippableEventState](avplayerinterstitialeventmonitor/currenteventskippablestate.md)
  The skippable event state for the currentEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskippednotification)*