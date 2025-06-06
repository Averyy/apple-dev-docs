# playerViewDidStartPicture(inPicture:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that Picture in Picture playback started.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerViewDidStartPicture(inPicture playerView: AVPlayerView)
```

## Parameters

- `playerView`: The player view.

## See Also

- [func playerViewWillStartPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to start.
- [func playerViewWillStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to stop.
- [func playerViewDidStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewdidstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback stopped.
- [func playerView(AVPlayerView, failedToStartPictureInPictureWithError: any Error)](avplayerviewpictureinpicturedelegate/playerview(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate that Picture in Picture playback failed to start.
- [func playerView(AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:).md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture:))*