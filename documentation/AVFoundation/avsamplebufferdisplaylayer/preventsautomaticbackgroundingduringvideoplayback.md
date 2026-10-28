# preventsAutomaticBackgroundingDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var preventsAutomaticBackgroundingDuringVideoPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL preventsAutomaticBackgroundingDuringVideoPlayback;
```

## Discussion

The default value is [`true`](../../Swift/true.md), which indicates the system doesn’t automatically background an app while playing video. The value of this property doesn’t prevent the user from backgrounding an app.

> **Note**:  When enqueuing sample buffers for playback at the user’s request, set the value to [`true`](../../Swift/true.md), and when video playback isn’t the user’s primary focus, set it to [`false`](../../Swift/false.md).

## See Also

### Preventing backgrounding
- [var preventsDisplaySleepDuringVideoPlayback: Bool](./preventsdisplaysleepduringvideoplayback.md)
  A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback)*