# skipCurrentEvent()

**Framework**: AVFoundation  
**Kind**: method

Causes the playback of the currently playing interstital event to be abandoned.

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
func skipCurrentEvent()
```

#### Discussion

Note that coinciding events will NOT be skipped. This results in AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification being posted. Has no effect while the currentEvent is nil.

## See Also

- [var events: [AVPlayerInterstitialEvent]!](avplayerinterstitialeventcontroller/events.md)
  The current schedule of interstitial events.
- [func cancelCurrentEvent(withResumptionOffset: CMTime)](avplayerinterstitialeventcontroller/cancelcurrentevent(withresumptionoffset:).md)
  Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent())*