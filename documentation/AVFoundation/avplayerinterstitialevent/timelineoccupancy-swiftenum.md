# AVPlayerInterstitialEvent.TimelineOccupancy

**Framework**: AVFoundation  
**Kind**: enum

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

## Topics

### Values
- [AVPlayerInterstitialEvent.TimelineOccupancy.singlePoint](avplayerinterstitialevent/timelineoccupancy-swift.enum/singlepoint.md)
  The event occupies a single point on the integrated timeline.
- [AVPlayerInterstitialEvent.TimelineOccupancy.fill](avplayerinterstitialevent/timelineoccupancy-swift.enum/fill.md)
  The event fills the integrated timeline with the duration of this event.
### Initializers
- [init?(rawValue: Int)](avplayerinterstitialevent/timelineoccupancy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.property.md)
  An event’s occupancy on the integrated timeline.
- [var supplementsPrimaryContent: Bool](avplayerinterstitialevent/supplementsprimarycontent.md)
  A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [var contentMayVary: Bool](avplayerinterstitialevent/contentmayvary.md)
  A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [var plannedDuration: CMTime](avplayerinterstitialevent/plannedduration.md)
  The planned duration of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.enum)*