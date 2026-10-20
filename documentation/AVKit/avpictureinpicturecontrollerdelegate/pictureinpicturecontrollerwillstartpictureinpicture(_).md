# pictureInPictureControllerWillStartPictureInPicture(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) pictureInPictureControllerWillStartPictureInPicture:(AVPictureInPictureController *) pictureInPictureController;
```

## Mentions

- [Adopting Picture in Picture in a custom player](../adopting-picture-in-picture-in-a-custom-player.md)

## Parameters

- `pictureInPictureController`: The delegating controller.

## See Also

### Responding to Picture in Picture life cycle events
- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerdidstartpictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureController(AVPictureInPictureController, failedToStartPictureInPictureWithError: any Error)](./pictureinpicturecontroller%28_,failedtostartpictureinpicturewitherror%29.md)
  Tells the delegate that Picture in Picture failed to start.
- [func pictureInPictureControllerWillStopPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerwillstoppictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture is about to stop.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerdidstoppictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:))*