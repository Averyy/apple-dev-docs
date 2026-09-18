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

### Responding to full-screen events
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
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [Customizing the tvOS playback experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [struct VideoPlayer](videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewdelegate)*