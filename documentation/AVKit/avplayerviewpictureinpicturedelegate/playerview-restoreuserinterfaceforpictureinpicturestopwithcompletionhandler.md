# playerView(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate to restore the user interface before Picture in Picture playback stops.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `playerView`: The player view.
- `completionHandler`: The completion handler to call after you’ve restored the user interface.

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
- [func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart: AVPlayerView) -> Bool](avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:).md)
  Asks the delegate if the player view should miniaturize when Picture in Picture starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:))*