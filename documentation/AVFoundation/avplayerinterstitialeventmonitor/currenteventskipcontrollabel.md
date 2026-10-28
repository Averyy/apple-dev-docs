# currentEventSkipControlLabel

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The skip control label for the currentEvent.

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
var currentEventSkipControlLabel: String? { get }
```

```objc
@property (readonly, nullable) NSString * currentEventSkipControlLabel;
```

## Discussion

If a localizedStringsBundle has been set on the AVPlayerInterstitialEventController, and a skipControlLocalizedLabelBundleKey is set on the currentEvent, then this value will be the localized string that was matched to the event’s skipControlLocalizedLabelBundleKey for the corresponding system language in the supplied Bundle, if any. If currentEvent is nil, then the value will be nil.

## See Also

### Monitoring skipping
- [class let currentEventSkippableStateDidChangeNotification: NSNotification.Name](./currenteventskippablestatedidchangenotification.md)
  A notification that’s posted whenever the currentEventSkippableState of an AVPlayerInterstitialEventMonitor changes.
- [class let currentEventSkippableStateDidChangeEventKey: String](./currenteventskippablestatedidchangeeventkey.md)
  The dictionary key for the AVPlayerInterstitial event that had its skippable event state changed in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippableStateDidChangeStateKey: String](./currenteventskippablestatedidchangestatekey.md)
  The dictionary key for the skippable event state in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippableStateDidChangeSkipControlLabelKey: String](./currenteventskippablestatedidchangeskipcontrollabelkey.md)
  The dictionary key for the skip label of the event in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.
- [class let currentEventSkippedNotification: NSNotification.Name](./currenteventskippednotification.md)
  A notification that’s posted whenever an event was skipped via skip control.
- [class let currentEventSkippedEventKey: String](./currenteventskippedeventkey.md)
  The dictionary key for the AVPlayerInterstitialEvent that was skipped in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification.
- [var currentEventSkippableState: AVPlayerInterstitialEvent.SkippableEventState](./currenteventskippablestate.md)
  The skippable event state for the currentEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskipcontrollabel)*