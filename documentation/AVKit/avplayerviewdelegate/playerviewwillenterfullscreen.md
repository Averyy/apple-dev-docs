# playerViewWillEnterFullScreen(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate that the player view is about to enter full-screen mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func playerViewWillEnterFullScreen(_ playerView: AVPlayerView)
```

## Parameters

- `playerView`: The player view.

## See Also

- [func playerViewDidEnterFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidenterfullscreen(_:).md)
  Tells the delegate that the player view entered full-screen mode.
- [func playerViewWillExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewwillexitfullscreen(_:).md)
  Tells the delegate that the player view is about to exit full-screen mode.
- [func playerViewDidExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidexitfullscreen(_:).md)
  Tells the delegate that the player view exited full-screen mode.
- [func playerView(AVPlayerView, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:).md)
  Tells the delegate to restore the app’s user interface when exiting full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerviewwillenterfullscreen(_:))*