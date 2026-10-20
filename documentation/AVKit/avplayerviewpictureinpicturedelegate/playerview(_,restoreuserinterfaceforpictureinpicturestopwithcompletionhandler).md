# playerView(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to restore the user interface before Picture in Picture playback stops.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerView(_ playerView: AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
```

```objc
- (void) playerView:(AVPlayerView *) playerView restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:(void (^)(BOOL restored)) completionHandler;
```

## Parameters

- `playerView`: The player view.
- `completionHandler`: The completion handler to call after you’ve restored the user interface.

## See Also

### Responding to Picture in Picture playback events
- [func playerViewWillStartPicture(inPicture: AVPlayerView)](./playerviewwillstartpicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback is about to start.
- [func playerViewDidStartPicture(inPicture: AVPlayerView)](./playerviewdidstartpicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback started.
- [func playerViewWillStopPicture(inPicture: AVPlayerView)](./playerviewwillstoppicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback is about to stop.
- [func playerViewDidStopPicture(inPicture: AVPlayerView)](./playerviewdidstoppicture%28inpicture%29.md)
  Tells the delegate that Picture in Picture playback stopped.
- [func playerView(AVPlayerView, failedToStartPictureInPictureWithError: any Error)](./playerview%28_,failedtostartpictureinpicturewitherror%29.md)
  Tells the delegate that Picture in Picture playback failed to start.
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](./playerviewshouldautomaticallydismissatpicture%28inpicturestart%29.md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:))*