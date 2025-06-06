# suspensionReasonsThatTriggerWaiting

**Framework**: AVFoundation  
**Kind**: property

The reasons that cause a coordinator to suspend playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var suspensionReasonsThatTriggerWaiting: [AVCoordinatedPlaybackSuspension.Reason] { get set }
```

## See Also

- [func participantLimitForWaitingOutSuspensions(withReason: AVCoordinatedPlaybackSuspension.Reason) -> Int](avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason:).md)
  Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [func setParticipantLimit(Int, forWaitingOutSuspensionsWithReason: AVCoordinatedPlaybackSuspension.Reason)](avplaybackcoordinator/setparticipantlimit(_:forwaitingoutsuspensionswithreason:).md)
  Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [var pauseSnapsToMediaTimeOfOriginator: Bool](avplaybackcoordinator/pausesnapstomediatimeoforiginator.md)
  A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsthattriggerwaiting)*