# playbackCoordinator(_:didIssue:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate to seek to a new time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue seekCommand: AVDelegatingPlaybackCoordinatorSeekCommand, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func playbackCoordinator(_ coordinator: AVDelegatingPlaybackCoordinator, didIssue seekCommand: AVDelegatingPlaybackCoordinatorSeekCommand) async
```

```objc
- (void) playbackCoordinator:(AVDelegatingPlaybackCoordinator *) coordinator didIssueSeekCommand:(AVDelegatingPlaybackCoordinatorSeekCommand *) seekCommand completionHandler:(void (^)()) completionHandler;
```

## Discussion

The coordinator issues this command to perform a seek in the item timeline, potentially pausing playback in the process.

## Parameters

- `coordinator`: The playback coordinator that issues the command.
- `seekCommand`: The command to execute. Before performing it, verify that its [`expectedCurrentItemIdentifier`](../avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md) property value matches the item that you’re currently playing. If the command isn’t valid for the current item, ignore it and call the completion handler.
- `completionHandler`: A completion handler that your app must call when it finishes handling the command, either successfully or after beginning a suspension if it can’t handle the command currently.

  If the value of the command’s [`shouldBufferInAnticipationOfPlayback`](../avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.md) property is [`true`](../../Swift/true.md), call the completion handler only after the player is ready for playback.

## See Also

### Responding to commands
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPlayCommand, completionHandler: () -> Void)](./playbackcoordinator%28_,didissue,completionhandler%29-73p3a.md)
  Tells the delegate to match the playback rate to that of the group when the rate is nonzero.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPauseCommand, completionHandler: () -> Void)](./playbackcoordinator%28_,didissue,completionhandler%29-56t01.md)
  Tells the delegate to pause playback.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorBufferingCommand, completionHandler: () -> Void)](./playbackcoordinator%28_,didissue,completionhandler%29-btle.md)
  Tells the delegate to expect playback soon and to start buffering media data in preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y)*