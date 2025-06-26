# interstitialEventWasUnscheduledNotification

**Framework**: AVFoundation  
**Kind**: property

A notification that is posted whenever an AVPlayerInterstitialEvent with loaded assets was unscheduled prior to playing.

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
class let interstitialEventWasUnscheduledNotification: NSNotification.Name
```

#### Discussion

Carries a userInfo dictionary that can contain the following keys and values:

1. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey, with a value that indicates which AVPlayerInterstitialEvent was unscheduled.
2. AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey, with an NSError value. This key will only be present if the AVPlayerInterstitialEvent was unscheduled due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/interstitialeventwasunschedulednotification)*