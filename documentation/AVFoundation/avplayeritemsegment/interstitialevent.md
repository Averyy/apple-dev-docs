# interstitialEvent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The associated interstitial event for this segment.

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
var interstitialEvent: AVPlayerInterstitialEvent? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVPlayerInterstitialEvent * interstitialEvent;
```

#### Discussion

This value is `nil` for segments that represent playback of the primary item.

## See Also

### Inspecting the segment
- [var timeMapping: CMTimeMapping](./timemapping.md)
  The time mapping for this segment.
- [var loadedTimeRanges: [CMTimeRange]](./loadedtimeranges-879hc.md)
  The time ranges for the segment that have media data is readily available.
- [var startDate: Date?](./startdate.md)
  The date at which a segment starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/interstitialevent)*