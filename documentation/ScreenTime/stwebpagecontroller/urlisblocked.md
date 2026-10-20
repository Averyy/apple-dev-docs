# urlIsBlocked

**Framework**: Screen Time  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a parent or guardian has blocked the URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var urlIsBlocked: Bool { get }
```

```objc
@property (readonly) BOOL URLIsBlocked;
```

#### Discussion

When a parent or guardian blocks the webpage’s URL, the webpage controller displays a blocking UI and then sets this property to [`YES`](../../ObjectiveC/yes.md).

## See Also

### Instance properties
- [var suppressUsageRecording: Bool](./suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var url: URL?](./url.md)
  The URL for the webpage.
- [var urlIsPictureInPicture: Bool](./urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.
- [var urlIsPlayingVideo: Bool](./urlisplayingvideo.md)
  A Boolean that indicates whether there are one or more videos currently playing in the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/urlisblocked)*