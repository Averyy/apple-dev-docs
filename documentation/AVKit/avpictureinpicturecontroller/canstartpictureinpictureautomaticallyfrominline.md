# canStartPictureInPictureAutomaticallyFromInline

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- visionOS 1.0+

## Declaration

```swift
var canStartPictureInPictureAutomaticallyFromInline: Bool { get set }
```

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Discussion

Only set this value to [`true`](https://developer.apple.com/documentation/swift/true) for content that you intend to be the user’s primary focus.

## See Also

- [var canStopPictureInPicture: Bool](avpictureinpicturecontroller/canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [func startPictureInPicture()](avpictureinpicturecontroller/startpictureinpicture.md)
  Starts Picture in Picture, if possible.
- [func stopPictureInPicture()](avpictureinpicturecontroller/stoppictureinpicture.md)
  Stops Picture in Picture, if active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline)*