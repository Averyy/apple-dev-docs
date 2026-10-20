# playerViewController(_:failedToStartPictureInPictureWithError:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when Picture in Picture fails to start.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, failedToStartPictureInPictureWithError error: any Error)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController failedToStartPictureInPictureWithError:(NSError *) error;
```

## Parameters

- `playerViewController`: The player view controller.
- `error`: An error object that describes the failure.

## See Also

### Responding to Picture in Picture life cycle events
- [func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(AVPlayerViewController) -> Bool](./playerviewcontrollershouldautomaticallydismissatpictureinpicturestart%28_%29.md)
  Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [func playerViewControllerWillStartPictureInPicture(AVPlayerViewController)](./playerviewcontrollerwillstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to start.
- [func playerViewControllerDidStartPictureInPicture(AVPlayerViewController)](./playerviewcontrollerdidstartpictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture starts.
- [func playerViewControllerWillStopPictureInPicture(AVPlayerViewController)](./playerviewcontrollerwillstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture is about to stop.
- [func playerViewControllerDidStopPictureInPicture(AVPlayerViewController)](./playerviewcontrollerdidstoppictureinpicture%28_%29.md)
  Tells the delegate when Picture in Picture stops.
- [func playerViewController(AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](./playerviewcontroller%28_,restoreuserinterfaceforpictureinpicturestopwithcompletionhandler%29.md)
  Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:failedtostartpictureinpicturewitherror:))*