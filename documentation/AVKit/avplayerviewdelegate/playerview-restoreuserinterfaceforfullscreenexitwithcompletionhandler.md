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

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

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