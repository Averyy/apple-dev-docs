# preventsDisplaySleepDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
var preventsDisplaySleepDuringVideoPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL preventsDisplaySleepDuringVideoPlayback;
```

#### Discussion

Setting this property to [`false`](../../Swift/false.md) doesn’t force the display to sleep; it only stops preventing display sleep. Other apps or frameworks within your app may still be preventing display sleep for various reasons.

The default value is [`true`](../../Swift/true.md) in iOS, tvOS, and Mac Catalyst. The default value in macOS is [`false`](../../Swift/false.md).

> **Note**:  If you enqueue sample buffers for playback at the user’s request, you should ensure that you set the value of this property to [`true`](../../Swift/true.md). If your app isn’t displaying video as part of the user’s primary focus, set the value of this property to [`false`](../../Swift/false.md).

## See Also

### Preventing backgrounding
- [var preventsAutomaticBackgroundingDuringVideoPlayback: Bool](./preventsautomaticbackgroundingduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback)*