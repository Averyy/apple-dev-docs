# AVDelegatingPlaybackCoordinatorSeekOptions

**Framework**: AVFoundation  
**Kind**: struct

Constants that define seek options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct AVDelegatingPlaybackCoordinatorSeekOptions
```

## Topics

### Seek options
- [static var resumeImmediately: AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions/resumeimmediately.md)
  An option that Indicates that the coordinator needs to resume playback as soon as possible, regardless of other participant’s readiness or suspensions.
### Initializers
- [init(rawValue: UInt)](avdelegatingplaybackcoordinatorseekoptions/init(rawvalue:).md)
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
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekoptions)*