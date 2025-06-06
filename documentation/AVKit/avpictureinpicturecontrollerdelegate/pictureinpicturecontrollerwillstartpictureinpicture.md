# pictureInPictureControllerWillStartPictureInPicture(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that Picture in Picture is about to start.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func pictureInPictureControllerWillStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)
```

## Mentions

- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)

## Parameters

- `pictureInPictureController`: The delegating controller.

## See Also

- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureController(AVPictureInPictureController, failedToStartPictureInPictureWithError: any Error)](avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate that Picture in Picture failed to start.
- [func pictureInPictureControllerWillStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to stop.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:))*