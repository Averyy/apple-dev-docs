# timeMapping

**Framework**: AVFoundation  
**Kind**: property

The time mapping for this segment.

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
var timeMapping: CMTimeMapping { get }
```

#### Discussion

The time mapping’s source time range represents the start time and duration in the segment source’s timeline, either the primary item or interstitial event. The target time range represents the start time and duration in the integrated timeline. For interstitial events that occupy a single point, the target’s duration is [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero).

## See Also

- [var loadedTimeRanges: [CMTimeRange]](avplayeritemsegment/loadedtimeranges-879hc.md)
  The time ranges for the segment that have media data is readily available.
- [var startDate: Date?](avplayeritemsegment/startdate.md)
  The date at which a segment starts.
- [var interstitialEvent: AVPlayerInterstitialEvent?](avplayeritemsegment/interstitialevent.md)
  The associated interstitial event for this segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/timemapping)*