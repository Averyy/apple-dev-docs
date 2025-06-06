# loadedTimeRanges

**Framework**: AVFoundation  
**Kind**: property

The time ranges for the segment that have media data is readily available.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@nonobjc
var loadedTimeRanges: [CMTimeRange] { get }
```

#### Discussion

The loaded time ranges might be discontinuous.

## See Also

- [var timeMapping: CMTimeMapping](avplayeritemsegment/timemapping.md)
  The time mapping for this segment.
- [var startDate: Date?](avplayeritemsegment/startdate.md)
  The date at which a segment starts.
- [var interstitialEvent: AVPlayerInterstitialEvent?](avplayeritemsegment/interstitialevent.md)
  The associated interstitial event for this segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/loadedtimeranges-879hc)*