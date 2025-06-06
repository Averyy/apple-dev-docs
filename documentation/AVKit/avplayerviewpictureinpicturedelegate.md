# AVPlayerViewPictureInPictureDelegate

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to implement to respond to Picture in Picture playback events.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol AVPlayerViewPictureInPictureDelegate : NSObjectProtocol
```

## Topics

### Responding to Picture in Picture Playback Events
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
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:).md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var allowsPictureInPicturePlayback: Bool](avplayerview/allowspictureinpictureplayback.md)
  A Boolean value that determines whether the player view allows Picture in Picture playback.
- [var pictureInPictureDelegate: (any AVPlayerViewPictureInPictureDelegate)?](avplayerview/pictureinpicturedelegate.md)
  The Picture in Picture delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate)*