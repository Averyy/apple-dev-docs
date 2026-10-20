# playerViewController(_:willBeginFullScreenPresentationWithAnimationCoordinator:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the player view controller is about to start full-screen display.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator coordinator: any UIViewControllerTransitionCoordinator)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController willBeginFullScreenPresentationWithAnimationCoordinator:(id<UIViewControllerTransitionCoordinator>) coordinator;
```

#### Discussion

This method isn’t called if you embed the player view controller as a child of the presented view controller.

## Parameters

- `playerViewController`: The player view controller.
- `coordinator`: The transition coordinator to use when coordinating animations.

## See Also

### Responding to full-screen presentations
- [func playerViewController(AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](./playerviewcontroller%28_,willendfullscreenpresentationwithanimationcoordinator%29.md)
  Tells the delegate when the player view controller is about to end full-screen display.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](./playerviewcontroller%28_,restoreuserinterfaceforfullscreenexitwithcompletionhandler%29.md)
  Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:))*