# AVPlaybackCoordinator

**Framework**: Avfoundation  
**Kind**: class

An object that coordinates the playback of players in a connected group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlaybackCoordinator
```

#### Overview

The framework provides two playback coordinator subclasses that manage different types of player objects:

- [`AVPlayerPlaybackCoordinator`](avplayerplaybackcoordinator.md) coordinates the state of [`AVPlayer`](avplayer.md) objects. If your app uses [`AVPlayer`](avplayer.md), continue to use its standard interfaces to control playback. The coordinator intercepts changes to the player’s rate and time, and propagates them to other players in the group.
- [`AVDelegatingPlaybackCoordinator`](avdelegatingplaybackcoordinator.md) coordinates the state of custom player objects. If your app uses a custom player, such as one that renders media using [`AVSampleBufferDisplayLayer`](avsamplebufferdisplaylayer.md) and [`AVSampleBufferAudioRenderer`](avsamplebufferaudiorenderer.md), use this object to coordinate group playback. Adopt the coordinator’s delegate protocol so that your player responds to the commands that the coordinator issues.

> **Note**:  Use the [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) framework to connect a playback coordinator to its peers.

## Topics

### Configuring Playback Policies
- [func participantLimitForWaitingOutSuspensions(withReason: AVCoordinatedPlaybackSuspension.Reason) -> Int](avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason:).md)
  Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [func setParticipantLimit(Int, forWaitingOutSuspensionsWithReason: AVCoordinatedPlaybackSuspension.Reason)](avplaybackcoordinator/setparticipantlimit(_:forwaitingoutsuspensionswithreason:).md)
  Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [var suspensionReasonsThatTriggerWaiting: [AVCoordinatedPlaybackSuspension.Reason]](avplaybackcoordinator/suspensionreasonsthattriggerwaiting.md)
  The reasons that cause a coordinator to suspend playback.
- [var pauseSnapsToMediaTimeOfOriginator: Bool](avplaybackcoordinator/pausesnapstomediatimeoforiginator.md)
  A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.
### Suspending State Coordination
- [func beginSuspension(for: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension](avplaybackcoordinator/beginsuspension(for:).md)
  Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [class AVCoordinatedPlaybackSuspension](avcoordinatedplaybacksuspension.md)
  An object that represents a temporary suspension of coordinated playback.
- [func expectedItemTime(atHostTime: CMTime) -> CMTime](avplaybackcoordinator/expecteditemtime(athosttime:).md)
  Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.
### Observing Suspension Reasons
- [var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason]](avplaybackcoordinator/suspensionreasons.md)
  The reasons a coordinator is currently unable to participate in a group playback activity.
- [class let suspensionReasonsDidChangeNotification: NSNotification.Name](avplaybackcoordinator/suspensionreasonsdidchangenotification.md)
  A notification that the coordinator posts when its suspension reasons change.
### Observing Other Participants
- [var otherParticipants: [AVCoordinatedPlaybackParticipant]](avplaybackcoordinator/otherparticipants.md)
  The identifiers of the other participants in a group.
- [class AVCoordinatedPlaybackParticipant](avcoordinatedplaybackparticipant.md)
  An object that represents a participant in a coordinated playback session.
- [class let otherParticipantsDidChangeNotification: NSNotification.Name](avplaybackcoordinator/otherparticipantsdidchangenotification.md)
  A notification that the coordinator posts when its other participants change.
### Coordinating with Group Sessions
- [func coordinateWithSession<T>(GroupSession<T>)](avplaybackcoordinator/coordinatewithsession(_:).md)
  Begins coordination of a player with a group session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md)
- [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Supporting Coordinated Media Playback](supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [class AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of player objects in a connected group.
- [class AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md)
  A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation/avplaybackcoordinator)*