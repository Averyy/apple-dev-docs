# playerViewWillExitFullScreen(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the player view is about to exit full-screen mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func playerViewWillExitFullScreen(_ playerView: AVPlayerView)
```

```objc
- (void) playerViewWillExitFullScreen:(AVPlayerView *) playerView;
```

## Parameters

- `playerView`: The player view.

## See Also

### Responding to full-screen events
- [func playerViewWillEnterFullScreen(AVPlayerView)](./playerviewwillenterfullscreen%28_%29.md)
  Tells the delegate that the player view is about to enter full-screen mode.
- [func playerViewDidEnterFullScreen(AVPlayerView)](./playerviewdidenterfullscreen%28_%29.md)
  Tells the delegate that the player view entered full-screen mode.
- [func playerViewDidExitFullScreen(AVPlayerView)](./playerviewdidexitfullscreen%28_%29.md)
  Tells the delegate that the player view exited full-screen mode.
- [func playerView(AVPlayerView, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](./playerview%28_,restoreuserinterfaceforfullscreenexitwithcompletionhandler%29.md)
  Tells the delegate to restore the app’s user interface when exiting full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerviewwillexitfullscreen(_:))*