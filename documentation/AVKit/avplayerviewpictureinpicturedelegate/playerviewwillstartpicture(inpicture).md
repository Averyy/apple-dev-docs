# playerViewWillStartPicture(inPicture:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that Picture in Picture playback is about to start.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerViewWillStartPicture(inPicture playerView: AVPlayerView)
```

```objc
- (void) playerViewWillStartPictureInPicture:(AVPlayerView *) playerView;
```

## Parameters

- `playerView`: The player view.

## See Also

### Responding to Picture in Picture playback events
- [func playerViewDidStartPicture(inPicture: AVPlayerView)](./playerviewdidstartpicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback started.
- [func playerViewWillStopPicture(inPicture: AVPlayerView)](./playerviewwillstoppicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback is about to stop.
- [func playerViewDidStopPicture(inPicture: AVPlayerView)](./playerviewdidstoppicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback stopped.
- [func playerView(AVPlayerView, failedToStartPictureInPictureWithError: any Error)](./playerview%28_,failedtostartpictureinpicturewitherror%29.md)
  Tells the delegate that Picture in Picture playback failed to start.
- [func playerView(AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](./playerview%28_,restoreuserinterfaceforpictureinpicturestopwithcompletionhandler%29.md)
  Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](./playerviewshouldautomaticallydismissatpicture%28inpicturestart%29.md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:))*