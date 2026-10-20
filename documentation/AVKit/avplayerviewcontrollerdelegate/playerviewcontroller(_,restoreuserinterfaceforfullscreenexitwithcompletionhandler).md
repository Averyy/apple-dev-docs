# playerViewController(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
optional func playerViewControllerRestoreUserInterfaceForFullScreenExit(_ playerViewController: AVPlayerViewController) async -> Bool
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController restoreUserInterfaceForFullScreenExitWithCompletionHandler:(void (^)(BOOL restored)) completionHandler;
```

## Parameters

- `playerViewController`: The player view controller.
- `completionHandler`: The completion handler to call for the system to finish restoring your user interface. You must invoke this callback with a value of `true`.

## See Also

### Responding to full-screen presentations
- [func playerViewController(AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](./playerviewcontroller%28_,willbeginfullscreenpresentationwithanimationcoordinator%29.md)
  Tells the delegate when the player view controller is about to start full-screen display.
- [func playerViewController(AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator: any UIViewControllerTransitionCoordinator)](./playerviewcontroller%28_,willendfullscreenpresentationwithanimationcoordinator%29.md)
  Tells the delegate when the player view controller is about to end full-screen display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:))*