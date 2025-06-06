# pictureInPictureController(_:failedToStartPictureInPictureWithError:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that Picture in Picture failed to start.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: any Error)
```

## Parameters

- `pictureInPictureController`: The delegating controller.
- `error`: An error that describes the details of the failure.

## See Also

- [func pictureInPictureControllerWillStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to start.
- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureControllerWillStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to stop.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:))*