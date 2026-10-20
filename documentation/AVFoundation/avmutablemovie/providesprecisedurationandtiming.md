# providesPreciseDurationAndTiming

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset provides precise duration and timing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var providesPreciseDurationAndTiming: Bool { get }
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you initialized the asset with the [`AVURLAssetPreferPreciseDurationAndTimingKey`](../avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [`false`](../../Swift/false.md).

## See Also

### Accessing duration and timing
- [var duration: CMTime](./duration.md)
  A time value that indicates the asset’s duration.
- [var minimumTimeOffsetFromLive: CMTime](./minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/providesprecisedurationandtiming)*