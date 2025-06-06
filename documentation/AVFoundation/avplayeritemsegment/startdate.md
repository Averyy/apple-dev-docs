# startDate

**Framework**: AVFoundation  
**Kind**: property

The date at which a segment starts.

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
var startDate: Date? { get }
```

#### Discussion

This value is `nil` if the primary item doesn’t contain dates.

## See Also

- [var timeMapping: CMTimeMapping](avplayeritemsegment/timemapping.md)
  The time mapping for this segment.
- [var loadedTimeRanges: [CMTimeRange]](avplayeritemsegment/loadedtimeranges-879hc.md)
  The time ranges for the segment that have media data is readily available.
- [var interstitialEvent: AVPlayerInterstitialEvent?](avplayeritemsegment/interstitialevent.md)
  The associated interstitial event for this segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/startdate)*