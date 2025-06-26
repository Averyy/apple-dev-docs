# interstitialEventWasUnscheduledErrorKey

**Framework**: AVFoundation  
**Kind**: property

The dictionary key to indicate whether the event that was unscheduled was due to an error.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class let interstitialEventWasUnscheduledErrorKey: String
```

#### Discussion

The value corresponding to this key is of type NSError. This key only exists in the payload of AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification if the interstitial event was unscheduled due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulederrorkey)*