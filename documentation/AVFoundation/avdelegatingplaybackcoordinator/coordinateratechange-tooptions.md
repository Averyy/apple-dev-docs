# coordinateRateChange(to:options:)

**Framework**: AVFoundation  
**Kind**: method

Coordinates a rate change across all participants, waiting for others to become ready, if necessary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func coordinateRateChange(to rate: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions = [])
```

#### Discussion

When the rate changes from zero to nonzero, the coordinator may also wait for participant suspensions from the [`suspensionReasonsThatTriggerWaiting`](avplaybackcoordinator/suspensionreasonsthattriggerwaiting.md) property.

Don’t call this method if the rate change doesn’t affect the group, or if the group doesn’t have control over local playback temporarily. For example, don’t call the method for a pause that occurs due to an audio session interruption. In those cases, inform the coordinator by beginning a suspension with an appropriate reason.

The suspension stops the coordinator from issuing further commands to its delegate. After beginning a suspension, you can reconfigure your app’s playback object as necessary.

> **Note**:  Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

## Parameters

- `rate`: The playback rate for the group to use.
- `options`: Additional configuration of the rate change.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateratechange(to:options:))*