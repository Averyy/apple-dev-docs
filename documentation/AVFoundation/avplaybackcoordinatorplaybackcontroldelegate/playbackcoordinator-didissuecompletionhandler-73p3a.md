# playbackCoordinator(_:didIssue:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate to match the playback rate to that of the group when the rate is nonzero.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue playCommand: AVDelegatingPlaybackCoordinatorPlayCommand) async
```

## Parameters

- `coordinator`: The playback coordinator that issues the command.
- `playCommand`: The command to execute. Before performing it, verify that its   property value matches the item that you’re currently playing. If the command isn’t valid for the current item, ignore it and call the completion handler.
- `completionHandler`: A completion handler that your app must call when it finishes handling the command, either successfully or after beginning a suspension if it can’t handle the command currently.

## See Also

- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPauseCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-56t01.md)
  Tells the delegate to pause playback.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorSeekCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y.md)
  Tells the delegate to seek to a new time.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorBufferingCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-btle.md)
  Tells the delegate to expect playback soon and to start buffering media data in preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-73p3a)*