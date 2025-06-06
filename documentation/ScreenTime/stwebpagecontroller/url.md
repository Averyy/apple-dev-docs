# url

**Framework**: Screen Time  
**Kind**: property

The URL for the webpage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
var url: URL? { get set }
```

#### Discussion

Set this value to the webpage’s URL when the user navigates to a new URL.

## See Also

- [var suppressUsageRecording: Bool](stwebpagecontroller/suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var urlIsBlocked: Bool](stwebpagecontroller/urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPictureInPicture: Bool](stwebpagecontroller/urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.
- [var urlIsPlayingVideo: Bool](stwebpagecontroller/urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/url)*