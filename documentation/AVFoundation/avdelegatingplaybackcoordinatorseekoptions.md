# AVDelegatingPlaybackCoordinatorSeekOptions

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVDelegatingPlaybackCoordinatorSeekOptions : NSUInteger;
```

## Topics

### Seek options
- [static var resumeImmediately: AVDelegatingPlaybackCoordinatorSeekOptions](./avdelegatingplaybackcoordinatorseekoptions/resumeimmediately.md)
  An option that Indicates that the coordinator needs to resume playback as soon as possible, regardless of other participant’s readiness or suspensions.
### Initializers
- [init(rawValue: UInt)](./avdelegatingplaybackcoordinatorseekoptions/init%28rawvalue%29.md)
  Creates a rate change option with a string.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Coordinating state changes
- [func coordinateRateChange(to: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions)](./avdelegatingplaybackcoordinator/coordinateratechange%28to,options%29.md)
  Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [func coordinateSeek(to: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions)](./avdelegatingplaybackcoordinator/coordinateseek%28to,options%29.md)
  Coordinates a seek to the specified time for all connected participants.
- [func transitionToItem(withIdentifier: String?, proposingInitialTimingBasedOn: CMTimebase?)](./avdelegatingplaybackcoordinator/transitiontoitem%28withidentifier,proposinginitialtimingbasedon%29.md)
  Tells the coordinator to transition to a new item.
- [func reapplyCurrentItemStateToPlaybackControlDelegate()](./avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate%28%29.md)
  Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [struct AVDelegatingPlaybackCoordinatorRateChangeOptions](./avdelegatingplaybackcoordinatorratechangeoptions.md)
  Constants that define rate change options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekoptions)*