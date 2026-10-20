# urlIsPlayingVideo

**Framework**: Screen Time  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether there are one or more videos currently playing in the webpage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var urlIsPlayingVideo: Bool { get set }
```

```objc
@property (nonatomic) BOOL URLIsPlayingVideo;
```

#### Discussion

The default value is [`NO`](../../ObjectiveC/no.md). Set this value when the webpage starts or stops playing video.

> ❗ **Important**: Set this value to [`NO`](../../ObjectiveC/no.md) prior to changing [`url`](./url.md) if the new webpage at that URL stops currently playing media and won’t immediately start playing new media.

## See Also

### Instance properties
- [var suppressUsageRecording: Bool](./suppressusagerecording.md)
  A Boolean that indicates whether the webpage controller is not recording web usage.
- [var url: URL?](./url.md)
  The URL for the webpage.
- [var urlIsBlocked: Bool](./urlisblocked.md)
  A Boolean that indicates whether a parent or guardian has blocked the URL.
- [var urlIsPictureInPicture: Bool](./urlispictureinpicture.md)
  A Boolean that indicates whether the webpage is currently displaying a floating picture in picture window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/urlisplayingvideo)*