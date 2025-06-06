# isPictureInPictureSuspended

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPictureInPictureSuspended: Bool { get }
```

#### Discussion

The system suspends your app’s Picture in Picture session when another app, typically FaceTime, is using the feature. In this state, your video playback is active but paused and offscreen. Picture in Picture resumes automatically when the other app finishes using PiP.

## See Also

- [class func isPictureInPictureSupported() -> Bool](avpictureinpicturecontroller/ispictureinpicturesupported.md)
  Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [var isPictureInPicturePossible: Bool](avpictureinpicturecontroller/ispictureinpicturepossible.md)
  A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [var isPictureInPictureActive: Bool](avpictureinpicturecontroller/ispictureinpictureactive.md)
  A Boolean value that indicates whether the Picture in Picture window is onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesuspended)*