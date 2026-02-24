# transitionToItem(withIdentifier:proposingInitialTimingBasedOn:)

**Framework**: AVFoundation  
**Kind**: method

Tells the coordinator to transition to a new item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func transitionToItem(withIdentifier itemIdentifier: String?, proposingInitialTimingBasedOn snapshotTimebase: CMTimebase?)
```

## Parameters

- `itemIdentifier`: The identifier for the new current item, which is `nil` if there isn’t anything to play.
- `snapshotTimebase`: A time base that communicates the initial playback state of the new item. If you specify `nil`, the coordinator assumes that the player pauses at [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero). You can retrieve an appropriate time base to pass for this value from AVFoundation playback objects like [`AVSampleBufferRenderSynchronizer`](avsamplebufferrendersynchronizer.md). You can also create one manually using the [`CMTimebaseCreateWithSourceClock(allocator:sourceClock:timebaseOut:)`](https://developer.apple.com/documentation/CoreMedia/CMTimebaseCreateWithSourceClock(allocator:sourceClock:timebaseOut:)) function.

## See Also

- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](avdelegatingplaybackcoordinator/coordinateratechange(to:options:).md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func coordinateSeek(to: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions)](avdelegatingplaybackcoordinator/coordinateseek(to:options:).md)
  Coordinates a seek to the specified time for all connected participants.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:))*