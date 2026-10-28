# currentEvent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current interstitial event.

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
var currentEvent: AVPlayerInterstitialEvent? { get }
```

```objc
@property (readonly, nullable) AVPlayerInterstitialEvent * currentEvent;
```

## Discussion

The value is `nil` when primary content is playing.

## See Also

### Monitoring the current event
- [class let currentEventDidChangeNotification: NSNotification.Name](./currenteventdidchangenotification.md)
  A notification the system posts when the monitor’s current interstitial event changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currentevent)*