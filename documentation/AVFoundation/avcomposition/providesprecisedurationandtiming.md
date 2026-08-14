# providesPreciseDurationAndTiming

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset provides precise duration and timing.

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
var providesPreciseDurationAndTiming: Bool { get }
```

#### Discussion

This property value is [`true`](https://developer.apple.com/documentation/swift/true) if you initialized the asset with the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var duration: CMTime](avcomposition/duration.md)
  A time value that indicates the asset’s duration.
- [var minimumTimeOffsetFromLive: CMTime](avcomposition/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/providesprecisedurationandtiming)*