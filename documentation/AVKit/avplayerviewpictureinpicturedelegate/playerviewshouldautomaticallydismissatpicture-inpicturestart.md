# playerViewShouldAutomaticallyDismissAtPicture(inPictureStart:)

**Framework**: AVKit  
**Kind**: method

Asks the delegate if the player view should miniaturize when Picture in Picture starts.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart playerView: AVPlayerView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the player view should automatically be miniaturized; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `playerView`: The player view.

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
- [func playerView(AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Void)](avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:).md)
  Tells the delegate to restore the user interface before Picture in Picture playback stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:))*