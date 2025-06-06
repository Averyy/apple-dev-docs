# playerViewControllerDidStopPictureInPicture(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when Picture in Picture stops.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewControllerDidStopPictureInPicture(_ playerViewController: AVPlayerViewController)
```

## Mentions

- [Adopting Picture in Picture in a Standard Player](adopting-picture-in-picture-in-a-standard-player.md)

#### Discussion

Don’t restore your app’s user interface in your implementation of this method. Instead, do it in the [`playerViewController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)`](avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md) method.

## Parameters

- `playerViewController`: The player view controller.

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
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(_:))*