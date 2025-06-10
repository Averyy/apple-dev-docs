# InterstitialEvent

**Framework**: AVKit  
**Kind**: struct

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct InterstitialEvent
```

## Topics

### Initializers
- [init(range: Range<TimeInterval>)](interstitialevent/init(range:).md)
### Instance Properties
- [var occupancyStyle: InterstitialEvent.OccupancyStyle](interstitialevent/occupancystyle-swift.property.md)
  Indicates occupancy type on the timeline
- [var range: Range<TimeInterval>](interstitialevent/range.md)
  The intersitial ranges that should be drawn on the timeline. Time intervals should  be normalized and instead be between `0.0..<duration`
- [var supplementsPrimaryContent: Bool](interstitialevent/supplementsprimarycontent.md)
  Indicates if content supports primary content and should not be colored
### Enumerations
- [InterstitialEvent.OccupancyStyle](interstitialevent/occupancystyle-swift.enum.md)
  Corresponds to AVPlayerInterstitialEvent.TimelineOccupancy

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var PLATFORM_SUPPORTS_AVKITCORE: Bool](platform_supports_avkitcore.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/interstitialevent)*