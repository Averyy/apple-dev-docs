# pictureInPictureControllerWillStopPictureInPicture(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that Picture in Picture is about to stop.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func pictureInPictureControllerWillStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)
```

## Parameters

- `pictureInPictureController`: The delegating controller.

## See Also

- [func pictureInPictureControllerWillStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to start.
- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureController(AVPictureInPictureController, failedToStartPictureInPictureWithError: any Error)](avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate that Picture in Picture failed to start.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:))*