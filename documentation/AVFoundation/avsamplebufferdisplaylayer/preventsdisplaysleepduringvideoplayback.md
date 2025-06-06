# preventsDisplaySleepDuringVideoPlayback

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) doesn’t force the display to sleep; it only stops preventing display sleep. Other apps or frameworks within your app may still be preventing display sleep for various reasons.

The default value is [`true`](https://developer.apple.com/documentation/swift/true) in iOS, tvOS, and Mac Catalyst. The default value in macOS is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  If you enqueue sample buffers for playback at the user’s request, you should ensure that you set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true). If your app isn’t displaying video as part of the user’s primary focus, set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false).

 If you enqueue sample buffers for playback at the user’s request, you should ensure that you set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true). If your app isn’t displaying video as part of the user’s primary focus, set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var preventsAutomaticBackgroundingDuringVideoPlayback: Bool](avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback)*