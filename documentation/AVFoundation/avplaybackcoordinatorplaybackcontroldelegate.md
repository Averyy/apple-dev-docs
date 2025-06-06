# AVPlaybackCoordinatorPlaybackControlDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the method to implement to respond to playback commands from the playback coordinator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVPlaybackCoordinatorPlaybackControlDelegate : NSObjectProtocol, Sendable
```

## Topics

### Responding to Commands
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPlayCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-73p3a.md)
  Tells the delegate to match the playback rate to that of the group when the rate is nonzero.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorPauseCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-56t01.md)
  Tells the delegate to pause playback.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorSeekCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-4fk8y.md)
  Tells the delegate to seek to a new time.
- [func playbackCoordinator(AVDelegatingPlaybackCoordinator, didIssue: AVDelegatingPlaybackCoordinatorBufferingCommand, completionHandler: () -> Void)](avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(_:didissue:completionhandler:)-btle.md)
  Tells the delegate to expect playback soon and to start buffering media data in preparation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(playbackControlDelegate: any AVPlaybackCoordinatorPlaybackControlDelegate)](avdelegatingplaybackcoordinator/init(playbackcontroldelegate:).md)
  Creates a playback coordinator for a custom playback object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate)*