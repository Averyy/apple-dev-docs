# startPictureInPicture()

**Framework**: AVKit  
**Kind**: method

Starts Picture in Picture, if possible.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func startPictureInPicture()
```

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Discussion

When you call this method and Picture in Picture (PiP) is possible, your delegate receives a call to its [`pictureInPictureControllerWillStartPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:).md) method. After a successful start, your delegate receives a call to the [`pictureInPictureControllerDidStartPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:).md) method.

If PiP fails, your delegate receives a call to the [`pictureInPictureController(_:failedToStartPictureInPictureWithError:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:).md)method.

Whether you explicitly stop PiP, the user stops it through interaction, or the system stops it, your delegate receives a call to the [`pictureInPictureControllerWillStopPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:).md) method, followed by the [`pictureInPictureControllerDidStopPictureInPicture(_:)`](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md) method after the PiP stop animation completes.

## See Also

- [var canStopPictureInPicture: Bool](avpictureinpicturecontroller/canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func stopPictureInPicture()](avpictureinpicturecontroller/stoppictureinpicture.md)
  Stops Picture in Picture, if active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/startpictureinpicture())*