# duration

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates the asset’s duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var duration: CMTime { get }
```

#### Discussion

If you initialized the composition’s assets by passing the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [`providesPreciseDurationAndTiming`](avasset/providesprecisedurationandtiming.md) property.

## See Also

- [var providesPreciseDurationAndTiming: Bool](avmutablemovie/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [var minimumTimeOffsetFromLive: CMTime](avmutablemovie/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/duration)*