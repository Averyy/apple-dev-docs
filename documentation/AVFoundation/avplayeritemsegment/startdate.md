# startDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSDate * startDate;
```

#### Discussion

This value is `nil` if the primary item doesn’t contain dates.

## See Also

### Inspecting the segment
- [var timeMapping: CMTimeMapping](./timemapping.md)
  The time mapping for this segment.
- [var loadedTimeRanges: [CMTimeRange]](./loadedtimeranges-879hc.md)
  The time ranges for the segment that have media data is readily available.
- [var interstitialEvent: AVPlayerInterstitialEvent?](./interstitialevent.md)
  The associated interstitial event for this segment.
- [loadedTimeRanges](./loadedtimeranges-2p0fl.md)
  The time ranges for the segment that have media data is readily available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/startdate)*