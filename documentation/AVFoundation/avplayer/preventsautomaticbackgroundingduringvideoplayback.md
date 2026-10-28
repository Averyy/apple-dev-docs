# preventsAutomaticBackgroundingDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
var preventsAutomaticBackgroundingDuringVideoPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL preventsAutomaticBackgroundingDuringVideoPlayback;
```

## Discussion

The default value is [`true`](../../Swift/true.md), which indicates the system doesn’t automatically background an app while it’s actively playing video. A user may still choose to background an app.

## See Also

### Preventing sleep and backgrounding
- [var preventsDisplaySleepDuringVideoPlayback: Bool](./preventsdisplaysleepduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents display and device sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preventsautomaticbackgroundingduringvideoplayback)*