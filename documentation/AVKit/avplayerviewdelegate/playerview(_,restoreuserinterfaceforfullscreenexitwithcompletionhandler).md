# playerView(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to restore the app’s user interface when exiting full-screen mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func playerView(_ playerView: AVPlayerView, restoreUserInterfaceForFullScreenExitWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
optional func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool
```

```objc
- (void) playerView:(AVPlayerView *) playerView restoreUserInterfaceForFullScreenExitWithCompletionHandler:(void (^)(BOOL restored)) completionHandler;
```

## Parameters

- `playerView`: The player view.
- `completionHandler`: You must call the completion handler with a value of `true` to allow the system to finish restoring your app’s user interface.

## See Also

### Responding to full-screen events
- [func playerViewWillEnterFullScreen(AVPlayerView)](./playerviewwillenterfullscreen%28_%29.md)
  Tells the delegate that the player view is about to enter full-screen mode.
- [func playerViewDidEnterFullScreen(AVPlayerView)](./playerviewdidenterfullscreen%28_%29.md)
  Tells the delegate that the player view entered full-screen mode.
- [func playerViewWillExitFullScreen(AVPlayerView)](./playerviewwillexitfullscreen%28_%29.md)
  Tells the delegate that the player view is about to exit full-screen mode.
- [func playerViewDidExitFullScreen(AVPlayerView)](./playerviewdidexitfullscreen%28_%29.md)
  Tells the delegate that the player view exited full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:))*