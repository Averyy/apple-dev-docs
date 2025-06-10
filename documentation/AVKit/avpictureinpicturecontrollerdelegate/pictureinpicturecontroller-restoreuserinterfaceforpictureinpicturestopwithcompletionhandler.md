# pictureInPictureController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate to restore the user interface before Picture in Picture stops.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController) async -> Bool
```

## Mentions

- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)

#### Discussion

Implement this method if your player user interface requires configuration or layout to return to its default state.

## Parameters

- `pictureInPictureController`: The delegating controller.
- `completionHandler`: You must call the completion handler with a value of   to allow the system to finish restoring your player user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:))*