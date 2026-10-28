# playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_ playerViewController: AVPlayerViewController) -> Bool
```

```objc
- (BOOL) playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:(AVPlayerViewController *) playerViewController;
```

## Return Value

`true` to indicate that the player view controller automatically dismisses itself; otherwise `false`.

## Discussion

Implement this method and return `false` to prevent the player view controller from automatically dismissing when Picture in Picture starts.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Responding to Picture in Picture life cycle events
- [func playerViewControllerWillStartPictureInPicture(AVPlayerViewController)](./playerviewcontrollerwillstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to start.
- [func playerViewControllerDidStartPictureInPicture(AVPlayerViewController)](./playerviewcontrollerdidstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture starts.
- [func playerViewController(AVPlayerViewController, failedToStartPictureInPictureWithError: any Error)](./playerviewcontroller%28_,failedtostartpictureinpicturewitherror%29.md)
  Tells the delegate when Picture in Picture fails to start.
- [func playerViewControllerWillStopPictureInPicture(AVPlayerViewController)](./playerviewcontrollerwillstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to stop.
- [func playerViewControllerDidStopPictureInPicture(AVPlayerViewController)](./playerviewcontrollerdidstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture stops.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](./playerviewcontroller%28_,restoreuserinterfaceforpictureinpicturestopwithcompletionhandler%29.md)
  Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(_:))*