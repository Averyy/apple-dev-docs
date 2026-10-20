# reapplyCurrentItemStateToPlaybackControlDelegate()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reapplyCurrentItemStateToPlaybackControlDelegate()
```

```objc
- (void) reapplyCurrentItemStateToPlaybackControlDelegate;
```

## See Also

### Coordinating state changes
- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](./coordinateratechange%28to,options%29.md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func coordinateSeek(to: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions)](./coordinateseek%28to,options%29.md)
  Coordinates a seek to the specified time for all connected participants.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](./transitiontoitem%28withidentifier,proposinginitialtimingbasedon%29.md)
  Tells the coordinator to transition to a new item.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate())*