# isPictureInPictureSupported()

**Framework**: AVKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the current device supports Picture in Picture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func isPictureInPictureSupported() -> Bool
```

```objc
+ (BOOL) isPictureInPictureSupported;
```

## Mentions

- [Adopting Picture in Picture for video calls](../adopting-picture-in-picture-for-video-calls.md)
- [Adopting Picture in Picture in a custom player](../adopting-picture-in-picture-in-a-custom-player.md)

#### Return Value

`true` if the current device supports Picture in Picture playback, otherwise `false`.

#### Discussion

If Picture in Picture isn’t supported on the current device, attempting to initialize a Picture in Picture controller returns `nil`.

## See Also

### Accessing Picture in Picture state
- [var isPictureInPicturePossible: Bool](./ispictureinpicturepossible.md)
  A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [var isPictureInPictureActive: Bool](./ispictureinpictureactive.md)
  A Boolean value that indicates whether the Picture in Picture window is onscreen.
- [var isPictureInPictureSuspended: Bool](./ispictureinpicturesuspended.md)
  A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesupported())*