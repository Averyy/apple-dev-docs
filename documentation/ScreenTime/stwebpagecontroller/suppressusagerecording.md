# suppressUsageRecording

**Framework**: Screen Time  
**Kind**: property

A Boolean that indicates whether the webpage controller is not recording web usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
var suppressUsageRecording: Bool { get set }
```

#### Discussion

Set to [`YES`](https://developer.apple.com/documentation/ObjectiveC/YES) to stop recording and reporting web-usage data.

## See Also

- [var url: URL?](stwebpagecontroller/url.md)
  The URL for the webpage.
- [var urlIsBlocked: Bool](stwebpagecontroller/urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPictureInPicture: Bool](stwebpagecontroller/urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.
- [var urlIsPlayingVideo: Bool](stwebpagecontroller/urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/suppressusagerecording)*