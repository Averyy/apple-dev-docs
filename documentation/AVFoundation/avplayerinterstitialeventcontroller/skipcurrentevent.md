# skipCurrentEvent()

**Framework**: AVFoundation  
**Kind**: method

Causes the playback of the currently playing interstital event to be abandoned.

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
func skipCurrentEvent()
```

#### Discussion

Note that coinciding events will NOT be skipped. This results in AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification being posted. Has no effect while the currentEvent is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent())*