# AVPlayerInterstitialEvent.TimelineOccupancy

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify how an event occupies time on an integrated timeline.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum TimelineOccupancy
```

```c
enum AVPlayerInterstitialEventTimelineOccupancy : NSInteger;
```

## Topics

### Values
- [AVPlayerInterstitialEvent.TimelineOccupancy.singlePoint](./timelineoccupancy-swift.enum/singlepoint.md)
  The event occupies a single point on the integrated timeline.
- [AVPlayerInterstitialEvent.TimelineOccupancy.fill](./timelineoccupancy-swift.enum/fill.md)
  The event fills the integrated timeline with the duration of this event.
### Initializers
- [init?(rawValue: Int)](./timelineoccupancy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting timeline occupancy
- [var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy](./timelineoccupancy-swift.property.md)
  An event’s occupancy on the integrated timeline.
- [var supplementsPrimaryContent: Bool](./supplementsprimarycontent.md)
  A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [var contentMayVary: Bool](./contentmayvary.md)
  A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [var plannedDuration: CMTime](./plannedduration.md)
  The planned duration of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.enum)*