# playerView(_:failedToStartPictureInPictureWithError:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that Picture in Picture playback failed to start.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerView(_ playerView: AVPlayerView, failedToStartPictureInPictureWithError error: any Error)
```

## Parameters

- `playerView`: The player view.
- `error`: An error object describing the failure.

## See Also

- [func playerViewWillStartPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to start.
- [func playerViewDidStartPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback started.
- [func playerViewWillStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewwillstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback is about to stop.
- [func playerViewDidStopPicture(inPicture: AVPlayerView)](avplayerviewpictureinpicturedelegate/playerviewdidstoppicture(inpicture:).md)
  Tells the delegate that Picture in Picture playback stopped.
- [func playerView(AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:).md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:failedtostartpictureinpicturewitherror:))*