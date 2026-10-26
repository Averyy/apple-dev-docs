# providesPreciseDurationAndTiming

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset provides precise duration and timing.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of  [`providesPreciseDurationAndTiming`](../avpartialasyncproperty/providesprecisedurationandtiming.md)  asynchronously instead. This property value is [`true`](../../Swift/true.md) if you initialized the asset with the [`AVURLAssetPreferPreciseDurationAndTimingKey`](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [`false`](../../Swift/false.md).
>
> #### Discussion

## Declaration

```swift
var providesPreciseDurationAndTiming: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL providesPreciseDurationAndTiming;
```

## See Also

### Accessing duration and timing
- [duration](./duration.md)
  A time value that indicates the asset’s duration.
- [minimumTimeOffsetFromLive](./minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/providesprecisedurationandtiming)*