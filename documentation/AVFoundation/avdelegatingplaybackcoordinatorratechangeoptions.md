# AVDelegatingPlaybackCoordinatorRateChangeOptions

**Framework**: AVFoundation  
**Kind**: struct

Constants that define rate change options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct AVDelegatingPlaybackCoordinatorRateChangeOptions
```

## Topics

### Rate change options
- [static var playImmediately: AVDelegatingPlaybackCoordinatorRateChangeOptions](avdelegatingplaybackcoordinatorratechangeoptions/playimmediately.md)
  Indicates that the coordinator should begin playback as soon as possible, regardless of other participant’s readiness or suspensions.
### Initializers
- [init(rawValue: UInt)](avdelegatingplaybackcoordinatorratechangeoptions/init(rawvalue:).md)
  Creates a rate change option with a string.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](avdelegatingplaybackcoordinator/coordinateratechange(to:options:).md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func coordinateSeek(to: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions)](avdelegatingplaybackcoordinator/coordinateseek(to:options:).md)
  Coordinates a seek to the specified time for all connected participants.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:).md)
  Tells the coordinator to transition to a new item.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions.md)
  Constants that define seek options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorratechangeoptions)*