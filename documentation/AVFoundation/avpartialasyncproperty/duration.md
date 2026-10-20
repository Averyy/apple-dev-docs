# duration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A time value that represents the duration of the asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var duration: AVAsyncProperty<Root, CMTime> { get }
```

Available when `Root` inherits `AVAsset`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

If the value of [`providesPreciseDurationAndTiming`](./providesprecisedurationandtiming.md) is [`false`](../../Swift/false.md), the asset returns a best-available estimate of the duration. You can specify your preferred degree of precision for timing-related properties when you create an [`AVURLAsset`](../avurlasset.md) by passing a value for the [`AVURLAssetPreferPreciseDurationAndTimingKey`](../avurlassetpreferprecisedurationandtimingkey.md) initialization option.

## See Also

### Loading duration and timing
- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](./providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime>](./minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/duration)*