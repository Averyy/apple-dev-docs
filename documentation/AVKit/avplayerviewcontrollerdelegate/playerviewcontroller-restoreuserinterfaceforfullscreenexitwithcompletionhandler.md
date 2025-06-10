# playerViewController(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewControllerRestoreUserInterfaceForFullScreenExit(_ playerViewController: AVPlayerViewController) async -> Bool
```

## Parameters

- `playerViewController`: The player view controller.
- `completionHandler`: The completion handler to call for the system to finish restoring your user interface. You must invoke this callback with a value of  .

## See Also

- [func playerViewController(AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:).md)
  Tells the delegate when the player view controller is about to start full-screen display.
- [func playerViewController(AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willendfullscreenpresentationwithanimationcoordinator:).md)
  Tells the delegate when the player view controller is about to end full-screen display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:))*