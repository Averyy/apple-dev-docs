# skipCurrentEvent()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) skipCurrentEvent;
```

#### Discussion

Note that coinciding events will NOT be skipped. This results in AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification being posted. Has no effect while the currentEvent is nil.

## See Also

### Configuring the event schedule
- [var events: [AVPlayerInterstitialEvent]!](./events.md)
  The current schedule of interstitial events.
- [func cancelCurrentEvent(withResumptionOffset: CMTime)](./cancelcurrentevent%28withresumptionoffset%29.md)
  Cancels the playback of all currently playing and scheduled interstitial events, and resumes playback of primary content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/skipcurrentevent())*