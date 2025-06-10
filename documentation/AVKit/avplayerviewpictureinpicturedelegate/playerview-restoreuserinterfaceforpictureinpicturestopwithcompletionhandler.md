# playerView(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate to restore the user interface before Picture in Picture playback stops.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
```

## Parameters

- `playerView`: The player view.
- `completionHandler`: The completion handler to call after you’ve restored the user interface.

## See Also

- [func playerViewWillStartPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to start.
- [func playerViewDidStartPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback started.
- [func playerViewWillStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to stop.
- [func playerViewDidStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewdidstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback stopped.
- [func playerView(AVPlayerView, failedToStartPictureInPictureWithError: any Error)](avplayerviewpictureinpicturedelegate/playerview(_:failedtostartpictureinpicturewitherror:).md)
  Tells the delegate that Picture in Picture playback failed to start.
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:).md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:))*