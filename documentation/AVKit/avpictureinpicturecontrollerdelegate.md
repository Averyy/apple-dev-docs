# AVPictureInPictureControllerDelegate

**Framework**: AVKit  
**Kind**: protocol

A protocol to adopt to respond to Picture in Picture events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVPictureInPictureControllerDelegate : NSObjectProtocol
```

## Mentions

- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)
- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Overview

Adopt this protocol in a custom object, and assign the object as the [`delegate`](avpictureinpicturecontroller/delegate.md) of your [`AVPictureInPictureController`](avpictureinpicturecontroller.md) instance.

## Topics

### Restoring the User Interface
- [func pictureInPictureController(AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate to restore the user interface before Picture in Picture stops.
### Responding to Picture in Picture Lifecycle Events
- [func pictureInPictureControllerWillStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to start.
- [func pictureInPictureControllerDidStartPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate that Picture in Picture started.
- [func pictureInPictureController(AVPictureInPictureController, failedToStartPictureInPictureWithError: any Error)](avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate that Picture in Picture failed to start.
- [func pictureInPictureControllerWillStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture is about to stop.
- [func pictureInPictureControllerDidStopPictureInPicture(AVPictureInPictureController)](avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate that Picture in Picture stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVPictureInPictureControllerDelegate)?](avpictureinpicturecontroller/delegate.md)
  A delegate object for a Picture in Picture controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate)*