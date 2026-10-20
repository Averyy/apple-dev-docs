# playerViewControllerWillStartPictureInPicture(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when Picture in Picture is about to start.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewControllerWillStartPictureInPicture(_ playerViewController: AVPlayerViewController)
```

```objc
- (void) playerViewControllerWillStartPictureInPicture:(AVPlayerViewController *) playerViewController;
```

## Mentions

- [Adopting Picture in Picture in a standard player](../adopting-picture-in-picture-in-a-standard-player.md)

#### Discussion

Implement this method to update your player user interface, such as hiding or disabling playback controls, prior to PiP starting.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Responding to Picture in Picture life cycle events
- [func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(AVPlayerViewController) -> Bool](./playerviewcontrollershouldautomaticallydismissatpictureinpicturestart%28_%29.md)
  Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(_:))*