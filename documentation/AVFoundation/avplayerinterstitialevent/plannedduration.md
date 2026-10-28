# plannedDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The planned duration of the event.

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
var plannedDuration: CMTime { get set }
```

```objc
@property (nonatomic, readwrite) CMTime plannedDuration;
```

## Discussion

The default value is [`zero`](../../CoreMedia/cmtime/zero.md).

## See Also

### Inspecting timeline occupancy
- [var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy](./timelineoccupancy-swift.property.md)
  An event’s occupancy on the integrated timeline.
- [AVPlayerInterstitialEvent.TimelineOccupancy](./timelineoccupancy-swift.enum.md)
  Constants that specify how an event occupies time on an integrated timeline.
- [var supplementsPrimaryContent: Bool](./supplementsprimarycontent.md)
  A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [var contentMayVary: Bool](./contentmayvary.md)
  A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/plannedduration)*