# AVPlayerPlaybackCoordinator

**Framework**: AVFoundation  
**Kind**: class

A playback coordinator subclass that coordinates the playback of player objects in a connected group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlayerPlaybackCoordinator
```

#### Overview

This object coordinates the state of [`AVPlayer`](avplayer.md) objects. You don’t create an instance of the coordinator, but instead access the player’s instance through its [`playbackCoordinator`](avplayer/playbackcoordinator.md) property.

Use the standard interfaces of [`AVPlayer`](avplayer.md) to control playback in your app. The coordinator automatically intercepts calls that affect transport control state, like [`setRate(_:time:atHostTime:)`](avplayer/setrate(_:time:athosttime:).md), [`pause()`](avplayer/pause().md), and [`seek(to:completionHandler:)`](avplayer/seek(to:completionhandler:)-75bls.md), and propagates them to other participants in the group when appropriate. Similarly, the coordinator observes rate and time changes from other participants and imposes them on the player. If this occurs, the player item posts notifications that identify the originating participant.

![A diagram representing two devices that each contain representations of the app, AVPlayer, AVPlayerItem, and AVPlayerPlaybackCoordinator relationships. The two AVPlayerPlaybackCoordinator items have a two-way dotted-line connection between the two devices.](https://docs-assets.developer.apple.com/published/7d8b117e91846756e31d0dac9c28a3d1/media-3839391%402x.png)

This object may automatically suspend coordinated playback when a system state change causes the player’s [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) value to change from a playing state to a waiting or paused state. A suspension that begins because the player enters a waiting state due to an event like a network stall or interstitial playback, ends automatically when the player finishes waiting. However, if the system pauses playback due to a system state change, such as an audio session interruption, the suspension ends only after the player’s rate changes back to nonzero.

> ❗ **Important**:  A playback coordinator doesn’t manage the playback queue of connected players. You need to implement custom logic to enqueue the same item across all connected players.

## Topics

### Accessing the player
- [var player: AVPlayer?](avplayerplaybackcoordinator/player.md)
  A player that participates in coordinated playback.
### Configuring the delegate
- [var delegate: (any AVPlayerPlaybackCoordinatorDelegate)?](avplayerplaybackcoordinator/delegate.md)
  A delegate object for the playback coordinator.
- [protocol AVPlayerPlaybackCoordinatorDelegate](avplayerplaybackcoordinatordelegate.md)
  A protocol that defines the methods to implement to participate in playback coordination.
### Managing coordination
- [func coordinate(using: AVPlaybackCoordinationMedium?) throws](avplayerplaybackcoordinator/coordinate(using:).md)
  Connects the playback coordinator to the coordination medium
- [var playbackCoordinationMedium: AVPlaybackCoordinationMedium?](avplayerplaybackcoordinator/playbackcoordinationmedium.md)
  The AVPlaybackCoordinationMedium this playback coordinator is connected to.

## Relationships

### Inherits From
- [AVPlaybackCoordinator](avplaybackcoordinator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Supporting coordinated media playback](supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [class AVPlaybackCoordinator](avplaybackcoordinator.md)
  An object that coordinates the playback of players in a connected group.
- [class AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.
- [class AVPlaybackCoordinationMedium](avplaybackcoordinationmedium.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator)*