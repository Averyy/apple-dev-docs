# playbackCoordinator(_:didIssue:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate to expect playback soon and to start buffering media data in preparation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue bufferingCommand: AVDelegatingPlaybackCoordinatorBufferingCommand) async
```

#### Discussion

The coordinator issues this command when playback is currently in a paused state and the coordinator is expecting playback to start soon. It provides an appropriate opportunity to update your player UI to indicate that playback is in a waiting state.

## Parameters

- `coordinator`: The playback coordinator that issues the command.
- `bufferingCommand`: The command to execute. Before performing it, verify that its   property value matches the item that you’re currently playing. If the command isn’t valid for the current item, ignore it and call the completion handler.
- `completionHandler`: If the value of the command’s   property is  , call the completion handler only after the player is ready for playback.

## See Also

- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPlayCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-73p3a.md)
  Tells the delegate to match the playback rate to that of the group when the rate is nonzero.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPauseCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-56t01.md)
  Tells the delegate to pause playback.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorSeekCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y.md)
  Tells the delegate to seek to a new time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-btle)*