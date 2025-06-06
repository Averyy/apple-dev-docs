# stopPictureInPicture()

**Framework**: AVKit  
**Kind**: method

Stops Picture in Picture, if active.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func stopPictureInPicture()
```

#### Discussion

Regardless of how Picture in Picture stops, the controller calls the delegate’s [`pictureInPictureControllerWillStopPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:).md) method. When the PiP animation completes, the controller finalizes the session by calling the delegate’s [`pictureInPictureControllerDidStopPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md) method.

## See Also

- [var canStopPictureInPicture: Bool](avpictureinpicturecontroller/canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](avpictureinpicturecontroller/startpictureinpicture.md)
  Starts Picture in Picture, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/stoppictureinpicture())*