# coordinateSeek(to:options:)

**Framework**: AVFoundation  
**Kind**: method

Coordinates a seek to the specified time for all connected participants.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func coordinateSeek(to time: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions = [])
```

#### Discussion

To end a suspension and also affect the group timing, see [`end(proposingNewTime:)`](avcoordinatedplaybacksuspension/end(proposingnewtime:).md).

> **Note**:  Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

 Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

## Parameters

- `time`: A time the group seeks to when the command ends.
- `options`: Additional configuration of the seek.

## See Also

- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](avdelegatingplaybackcoordinator/coordinateratechange(to:options:).md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:).md)
  Tells the coordinator to transition to a new item.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateseek(to:options:))*