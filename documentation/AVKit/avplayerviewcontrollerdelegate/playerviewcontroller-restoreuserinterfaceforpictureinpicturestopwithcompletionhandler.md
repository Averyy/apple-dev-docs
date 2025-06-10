# playerViewController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewControllerRestoreUserInterfaceForPictureInPictureStop(_ playerViewController: AVPlayerViewController) async -> Bool
```

## Mentions

- [Adopting Picture in Picture in a Standard Player](adopting-picture-in-picture-in-a-standard-player.md)

#### Discussion

Implement this method to reestablish your playback user interface when PiP ends. The framework calls this method no matter how PiP ends, whether it’s because the user ended playback, the user tapped the button to return ongoing video playback to your app, or the video finished playing on its own.

## Parameters

- `playerViewController`: The player view controller.
- `completionHandler`: You must call the completion handler with a value of   to allow the system to finish restoring your app’s user interface.

## See Also

- [func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(AVPlayerViewController) -> Bool](avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(_:).md)
  Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [func playerViewControllerWillStartPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(_:).md)
  Tells the delegate when Picture in Picture is about to start.
- [func playerViewControllerDidStartPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidstartpictureinpicture(_:).md)
  Tells the delegate when Picture in Picture starts.
- [func playerViewController(AVPlayerViewController, failedToStartPictureInPictureWithError: any Error)](avplayerviewcontrollerdelegate/playerviewcontroller(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate when Picture in Picture fails to start.
- [func playerViewControllerWillStopPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerwillstoppictureinpicture(_:).md)
  Tells the delegate when Picture in Picture is about to stop.
- [func playerViewControllerDidStopPictureInPicture(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(_:).md)
  Tells the delegate when Picture in Picture stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:))*