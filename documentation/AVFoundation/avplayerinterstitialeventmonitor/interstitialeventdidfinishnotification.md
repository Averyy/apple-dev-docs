# interstitialEventDidFinishNotification

**Framework**: AVFoundation  
**Kind**: property

A notification that is posted whenever an AVPlayerInterstitialEvent finished playing.

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
class let interstitialEventDidFinishNotification: NSNotification.Name
```

#### Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey, with a value that indicates the AVPlayerInterstitialEvent that finished playing.
2. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey, with a value that indicates how long that AVPlayerInterstitialEvent played out for.
3. AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey, with a value that indicates whether the AVPlayerInterstitialEvent was fully played out.

Note that cancelling an AVPlayerInterstitialEvent after playback started but prior to playback finishing will also trigger this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventdidfinishnotification)*