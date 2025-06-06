# duration

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates the asset’s duration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var duration: CMTime { get }
```

#### Discussion

If you initialized the composition’s assets by passing the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [`providesPreciseDurationAndTiming`](avasset/providesprecisedurationandtiming.md) property.

## See Also

- [var providesPreciseDurationAndTiming: Bool](avcomposition/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [var minimumTimeOffsetFromLive: CMTime](avcomposition/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/duration)*