# contentMayVary

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.

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
var contentMayVary: Bool { get set }
```

#### Discussion

If the value is [`false`](https://developer.apple.com/documentation/swift/false), the primary asset participates in coordinated playback, this event does as well.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.property.md)
  An event’s occupancy on the integrated timeline.
- [AVPlayerInterstitialEvent.TimelineOccupancy](avplayerinterstitialevent/timelineoccupancy-swift.enum.md)
  Constants that specify how an event occupies time on an integrated timeline.
- [var supplementsPrimaryContent: Bool](avplayerinterstitialevent/supplementsprimarycontent.md)
  A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [var plannedDuration: CMTime](avplayerinterstitialevent/plannedduration.md)
  The planned duration of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/contentmayvary)*