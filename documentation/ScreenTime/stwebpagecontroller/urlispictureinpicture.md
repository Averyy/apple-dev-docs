# urlIsPictureInPicture

**Framework**: Screen Time  
**Kind**: property

A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
var urlIsPictureInPicture: Bool { get set }
```

#### Discussion

The default value is [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO). Set this value when the webpage starts or stops displaying a Picture in Picture window.

> ❗ **Important**: Set this value to [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO) prior to changing [`url`](stwebpagecontroller/url.md) if the new webpage at that URL ends all currently displayed Picture in Picture windows, and won’t immediately display a new one.

## See Also

- [var suppressUsageRecording: Bool](stwebpagecontroller/suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var url: URL?](stwebpagecontroller/url.md)
  The URL for the webpage.
- [var urlIsBlocked: Bool](stwebpagecontroller/urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPlayingVideo: Bool](stwebpagecontroller/urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/urlispictureinpicture)*