# AVPlayerViewDelegate

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol AVPlayerViewDelegate : NSObjectProtocol
```

## Topics

### Responding to Full Screen Events
- [func playerViewWillEnterFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewwillenterfullscreen(_:).md)
  Tells the delegate that the player view is about to enter full-screen mode.
- [func playerViewDidEnterFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidenterfullscreen(_:).md)
  Tells the delegate that the player view entered full-screen mode.
- [func playerViewWillExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewwillexitfullscreen(_:).md)
  Tells the delegate that the player view is about to exit full-screen mode.
- [func playerViewDidExitFullScreen(AVPlayerView)](avplayerviewdelegate/playerviewdidexitfullscreen(_:).md)
  Tells the delegate that the player view exited full-screen mode.
- [func playerView(AVPlayerView, restoreUserInterfaceForFullScreenExitWithCompletionHandler: (Bool) -> Void)](avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:).md)
  Tells the delegate to restore the app’s user interface when exiting full-screen mode.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AVPlayerViewDelegate)?](avplayerview/delegate.md)
  The player view’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate)*