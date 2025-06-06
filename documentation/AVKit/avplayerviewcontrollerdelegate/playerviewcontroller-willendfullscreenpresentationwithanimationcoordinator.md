# playerViewController(_:willEndFullScreenPresentationWithAnimationCoordinator:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the player view controller is about to end full-screen display.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator coordinator: any UIViewControllerTransitionCoordinator)
```

## Parameters

- `playerViewController`: The player view controller.
- `coordinator`: The transition coordinator to use when coordinating animations.

## See Also

- [func playerViewController(AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:).md)
  Tells the delegate when the player view controller is about to start full-screen display.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:).md)
  Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willendfullscreenpresentationwithanimationcoordinator:))*