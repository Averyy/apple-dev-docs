# pauseSnapsToMediaTimeOfOriginator

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var pauseSnapsToMediaTimeOfOriginator: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL pauseSnapsToMediaTimeOfOriginator;
```

#### Discussion

If this value is [`true`](../../Swift/true.md), all participants seek to the originator’s stop time after they pause. Use this setting if it counteracts network delays that result from communicating the originator’s pause state to the other participants.

If this value is [`false`](../../Swift/false.md), it’s acceptable for participants to stop at slightly different times, and a pause doesn’t cause the time of other participants to jump back.

## See Also

### Configuring playback policies
- [func participantLimitForWaitingOutSuspensions(withReason: AVCoordinatedPlaybackSuspension.Reason) -> Int](./participantlimitforwaitingoutsuspensions%28withreason%29.md)
  Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [func setParticipantLimit(Int, forWaitingOutSuspensionsWithReason: AVCoordinatedPlaybackSuspension.Reason)](./setparticipantlimit%28_,forwaitingoutsuspensionswithreason%29.md)
  Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [var suspensionReasonsThatTriggerWaiting: [AVCoordinatedPlaybackSuspension.Reason]](./suspensionreasonsthattriggerwaiting.md)
  The reasons that cause a coordinator to suspend playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/pausesnapstomediatimeoforiginator)*