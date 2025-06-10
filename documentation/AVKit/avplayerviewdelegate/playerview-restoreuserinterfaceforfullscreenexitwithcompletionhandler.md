# playerView(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate to restore the app’s user interface when exiting full-screen mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool
```

## Parameters

- `playerView`: The player view.
- `completionHandler`: You must call the completion handler with a value of   to allow the system to finish restoring your app’s user interface.

## See Also

- [func playerViewWillEnterFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewwillenterfullscreen(_:).md)
  Tells the delegate that the player view is about to enter full-screen mode.
- [func playerViewDidEnterFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidenterfullscreen(_:).md)
  Tells the delegate that the player view entered full-screen mode.
- [func playerViewWillExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewwillexitfullscreen(_:).md)
  Tells the delegate that the player view is about to exit full-screen mode.
- [func playerViewDidExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidexitfullscreen(_:).md)
  Tells the delegate that the player view exited full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:))*