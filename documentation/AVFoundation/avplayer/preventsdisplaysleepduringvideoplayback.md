# preventsDisplaySleepDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether video playback prevents display and device sleep.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+

## Declaration

```swift
nonisolated
var preventsDisplaySleepDuringVideoPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL preventsDisplaySleepDuringVideoPlayback;
```

#### Discussion

The default value is [`true`](../../Swift/true.md) in iOS, tvOS and Mac Catalyst apps, and [`false`](../../Swift/false.md) in macOS.

Setting this property to [`false`](../../Swift/false.md) doesn’t force the display to sleep, it only stops preventing display sleep. Other apps, or frameworks within your app may still prevent display sleep for various reasons.

> **Note**:  Before macOS 13, iOS 16, tvOS 16, and watchOS 9, you can only access this property from the main thread or queue.

## See Also

### Preventing sleep and backgrounding
- [var preventsAutomaticBackgroundingDuringVideoPlayback: Bool](./preventsautomaticbackgroundingduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/preventsdisplaysleepduringvideoplayback)*