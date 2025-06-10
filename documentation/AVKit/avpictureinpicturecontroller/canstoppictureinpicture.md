# canStopPictureInPicture

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether Picture in Picture is active and is able to stop.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
var canStopPictureInPicture: Bool { get }
```

## Mentions

- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)

#### Discussion

When this value is `true`, calling [`stopPictureInPicture()`](avpictureinpicturecontroller/stoppictureinpicture().md) stops the active Picture in Picture session. Apps should update the state of UI that starts Picture in Picture when this property value changes.

Thie value is key-value observable.

## See Also

- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](avpictureinpicturecontroller/startpictureinpicture.md)
  Starts Picture in Picture, if possible.
- [func stopPictureInPicture()](avpictureinpicturecontroller/stoppictureinpicture.md)
  Stops Picture in Picture, if active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/canstoppictureinpicture)*