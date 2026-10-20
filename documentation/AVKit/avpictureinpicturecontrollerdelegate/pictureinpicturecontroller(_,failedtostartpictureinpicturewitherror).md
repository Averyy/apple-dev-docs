# pictureInPictureController(_:failedToStartPictureInPictureWithError:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) pictureInPictureController:(AVPictureInPictureController *) pictureInPictureController failedToStartPictureInPictureWithError:(NSError *) error;
```

## Parameters

- `pictureInPictureController`: The delegating controller.
- `error`: An error that describes the details of the failure.

## See Also

### Responding to Picture in Picture life cycle events
- [func pictureInPictureControllerWillStartPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerwillstartpictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture is about to start.
- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerdidstartpictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureControllerWillStopPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerwillstoppictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture is about to stop.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](./pictureinpicturecontrollerdidstoppictureinpicture%28_%29.md)
  Tells the delegate that Picture in Picture stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:))*