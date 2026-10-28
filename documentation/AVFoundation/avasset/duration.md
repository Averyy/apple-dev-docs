# duration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time value that indicates the asset’s duration.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`duration`](../avpartialasyncproperty/duration.md) asynchronously instead.

## Declaration

```swift
var duration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime duration;
```

## Discussion

If you initialized the asset by passing the [`AVURLAssetPreferPreciseDurationAndTimingKey`](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, this property value provides the asset’s precise duration; otherwise, it provides a best-available estimate. You can determine the value’s accuracy by querying the asset’s [`providesPreciseDurationAndTiming`](./providesprecisedurationandtiming.md) property.

## See Also

### Accessing duration and timing
- [providesPreciseDurationAndTiming](./providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](./minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/duration)*