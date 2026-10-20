# suspensionReasonsThatTriggerWaiting

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy) NSArray<NSString *> * suspensionReasonsThatTriggerWaiting;
```

## See Also

### Configuring playback policies
- [func participantLimitForWaitingOutSuspensions(withReason: AVCoordinatedPlaybackSuspension.Reason) -> Int](./participantlimitforwaitingoutsuspensions%28withreason%29.md)
  Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [func setParticipantLimit(Int, forWaitingOutSuspensionsWithReason: AVCoordinatedPlaybackSuspension.Reason)](./setparticipantlimit%28_,forwaitingoutsuspensionswithreason%29.md)
  Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [var pauseSnapsToMediaTimeOfOriginator: Bool](./pausesnapstomediatimeoforiginator.md)
  A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsthattriggerwaiting)*