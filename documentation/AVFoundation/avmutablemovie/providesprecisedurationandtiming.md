# providesPreciseDurationAndTiming

**Framework**: AVFoundation  
**Kind**: property

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

This property value is [`true`](https://developer.apple.com/documentation/Swift/true) if you initialized the asset with the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var duration: CMTime](avmutablemovie/duration.md)
  A time value that indicates the asset’s duration.
- [var minimumTimeOffsetFromLive: CMTime](avmutablemovie/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/providesprecisedurationandtiming)*