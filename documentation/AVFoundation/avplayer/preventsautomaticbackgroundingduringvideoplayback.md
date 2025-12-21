# preventsAutomaticBackgroundingDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
var preventsAutomaticBackgroundingDuringVideoPlayback: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true), which indicates the system doesn’t automatically background an app while it’s actively playing video. A user may still choose to background an app.

## See Also

- [var preventsDisplaySleepDuringVideoPlayback: Bool](avplayer/preventsdisplaysleepduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents display and device sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preventsautomaticbackgroundingduringvideoplayback)*