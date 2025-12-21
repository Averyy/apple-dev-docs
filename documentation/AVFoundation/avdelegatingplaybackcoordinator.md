# AVDelegatingPlaybackCoordinator

**Framework**: AVFoundation  
**Kind**: class

A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVDelegatingPlaybackCoordinator
```

#### Overview

This object coordinates the state of custom player objects, such as those that render media using [`AVSampleBufferDisplayLayer`](avsamplebufferdisplaylayer.md) and [`AVSampleBufferAudioRenderer`](avsamplebufferaudiorenderer.md), or that play audio using [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine).

Adopt the [`AVPlaybackCoordinatorPlaybackControlDelegate`](avplaybackcoordinatorplaybackcontroldelegate.md) protocol so that your app responds to playback commands from the coordinator. The commands provide the details of a requested state change so you can control your player object accordingly.

![A diagram representing two devices that each contain representations of the app, AVDelegatingPlaybackCoordinator, playback control delegate, and custom playback object relationships. The two AVDelegatingPlaybackCoordinator items have a two-way dotted-line connection between the two devices.](https://docs-assets.developer.apple.com/published/f1475dd7253b6e97cc096c2648300c98/media-3783472%402x.png)

## Topics

### Creating a coordinator
- [init(playbackControlDelegate: any AVPlaybackCoordinatorPlaybackControlDelegate)](avdelegatingplaybackcoordinator/init(playbackcontroldelegate:).md)
  Creates a playback coordinator for a custom playback object.
- [protocol AVPlaybackCoordinatorPlaybackControlDelegate](avplaybackcoordinatorplaybackcontroldelegate.md)
  A protocol that defines the method to implement to respond to playback commands from the playback coordinator.
### Identifying items
- [var currentItemIdentifier: String?](avdelegatingplaybackcoordinator/currentitemidentifier.md)
  An identifier of the current item.
### Accessing the delegate
- [var playbackControlDelegate: (any AVPlaybackCoordinatorPlaybackControlDelegate)?](avdelegatingplaybackcoordinator/playbackcontroldelegate.md)
  The delegate object for the playback coordinator.
### Coordinating state changes
- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](avdelegatingplaybackcoordinator/coordinateratechange(to:options:).md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func coordinateSeek(to: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions)](avdelegatingplaybackcoordinator/coordinateseek(to:options:).md)
  Coordinates a seek to the specified time for all connected participants.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:).md)
  Tells the coordinator to transition to a new item.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.
### Playback commands
- [class AVDelegatingPlaybackCoordinatorPlaybackControlCommand](avdelegatingplaybackcoordinatorplaybackcontrolcommand.md)
  An abstract superclass for playback commands.
- [class AVDelegatingPlaybackCoordinatorPlayCommand](avdelegatingplaybackcoordinatorplaycommand.md)
  A command that indicates to play at a specific rate and time.
- [class AVDelegatingPlaybackCoordinatorPauseCommand](avdelegatingplaybackcoordinatorpausecommand.md)
  A command that indicates to pause playback.
- [class AVDelegatingPlaybackCoordinatorSeekCommand](avdelegatingplaybackcoordinatorseekcommand.md)
  A command that indicates to seek to a new time in the item timeline.
- [class AVDelegatingPlaybackCoordinatorBufferingCommand](avdelegatingplaybackcoordinatorbufferingcommand.md)
  A command that indicates to start buffering data in preparation for playback.

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
- [class AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of player objects in a connected group.
- [class AVPlaybackCoordinationMedium](avplaybackcoordinationmedium.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator)*