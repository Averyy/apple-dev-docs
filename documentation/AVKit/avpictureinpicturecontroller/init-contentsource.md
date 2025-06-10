# init(contentSource:)

**Framework**: AVKit  
**Kind**: init

Creates a Picture in Picture controller with a content source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(contentSource: AVPictureInPictureController.ContentSource)
```

#### Discussion

Use this initializer to create a controller that displays its content in a player layer or a sample buffer display layer.

> ❗ **Important**:  Before attempting to create a controller, verify that the current device supports Picture in Picture by calling the [`isPictureInPictureSupported()`](avpictureinpicturecontroller/ispictureinpicturesupported().md) class method. Attempting to create a Picture in Picture controller on an unsupported device returns `nil`.

## Parameters

- `contentSource`: The source of the content to show in a Picture in Picture window.

## See Also

- [convenience init?(playerLayer: AVPlayerLayer)](avpictureinpicturecontroller/init(playerlayer:).md)
  Creates a Picture in Picture controller with a player layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/init(contentsource:))*