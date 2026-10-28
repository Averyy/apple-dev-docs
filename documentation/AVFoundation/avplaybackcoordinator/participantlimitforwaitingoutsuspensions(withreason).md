# participantLimitForWaitingOutSuspensions(withReason:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func participantLimitForWaitingOutSuspensions(withReason reason: AVCoordinatedPlaybackSuspension.Reason) -> Int
```

```objc
- (NSInteger) participantLimitForWaitingOutSuspensionsWithReason:(AVCoordinatedPlaybackSuspensionReason) reason;
```

## Return Value

The participant limit.

## Parameters

- `reason`: The suspension reason to find a participant limit for.

## See Also

### Configuring playback policies
- [func setParticipantLimit(Int, forWaitingOutSuspensionsWithReason: AVCoordinatedPlaybackSuspension.Reason)](./setparticipantlimit%28_,forwaitingoutsuspensionswithreason%29.md)
  Sets a limit on the number of partipants that a group may contain before the coordinator stops waiting on suspensions that occur for a particular reason.
- [var suspensionReasonsThatTriggerWaiting: [AVCoordinatedPlaybackSuspension.Reason]](./suspensionreasonsthattriggerwaiting.md)
  The reasons that cause a coordinator to suspend playback.
- [var pauseSnapsToMediaTimeOfOriginator: Bool](./pausesnapstomediatimeoforiginator.md)
  A Boolean value that indicates whether participants mirror the originator’s stop time when they pause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/participantlimitforwaitingoutsuspensions(withreason:))*