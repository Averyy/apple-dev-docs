# contentSource

**Framework**: AVKit  
**Kind**: property

The source of the controller’s content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var contentSource: AVPictureInPictureController.ContentSource? { get set }
```

#### Discussion

You can change a content source while a Picture in Picture session is active, but only if the new content source is ready for display. If it isn’t ready, the session ends immediately.

If your app uses [`AVPlayerLayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayerLayer), verify that the value of its [`isReadyForDisplay`](https://developer.apple.com/documentation/AVFoundation/AVPlayerLayer/isReadyForDisplay) property is `true` before setting it as a content source.

## See Also

- [AVPictureInPictureController.ContentSource](avpictureinpicturecontroller/contentsource-swift.class.md)
  An object that represents the source of the content to present in Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.property)*