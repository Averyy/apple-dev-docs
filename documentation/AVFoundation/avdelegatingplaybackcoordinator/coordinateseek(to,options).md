# coordinateSeek(to:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) coordinateSeekToTime:(CMTime) time options:(AVDelegatingPlaybackCoordinatorSeekOptions) options;
```

#### Discussion

To end a suspension and also affect the group timing, see [`end(proposingNewTime:)`](../avcoordinatedplaybacksuspension/end%28proposingnewtime%29.md).

> **Note**:  Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

## Parameters

- `time`: A time the group seeks to when the command ends.
- `options`: Additional configuration of the seek.

## See Also

### Coordinating state changes
- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](./coordinateratechange%28to,options%29.md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](./transitiontoitem%28withidentifier,proposinginitialtimingbasedon%29.md)
  Tells the coordinator to transition to a new item.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](./reapplycurrentitemstatetoplaybackcontroldelegate%28%29.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateseek(to:options:))*