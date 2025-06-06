# init(videoDisplay:)

**Framework**: AVFoundation  
**Kind**: init

Creates a rendered legible output object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
init(videoDisplay videoDisplaySize: CGSize)
```

#### Discussion

You can also choose to reset the [`videoDisplaySize`](avplayeritemrenderedlegibleoutput/videodisplaysize.md) value after initialization or during playback.

> ❗ **Important**:  Attempting to set a video display size of [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGSize/zero) results in the system throwing an exception.

 Attempting to set a video display size of [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGSize/zero) results in the system throwing an exception.

## Parameters

- `videoDisplaySize`: The size of the video display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/init(videodisplay:))*