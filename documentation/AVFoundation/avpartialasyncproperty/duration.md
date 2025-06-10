# duration

**Framework**: AVFoundation  
**Kind**: property

A time value that represents the duration of the asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var duration: AVAsyncProperty<Root, CMTime> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

If the value of [`providesPreciseDurationAndTiming`](avpartialasyncproperty/providesprecisedurationandtiming.md) is [`false`](https://developer.apple.com/documentation/swift/false), the asset returns a best-available estimate of the duration. You can specify your preferred degree of precision for timing-related properties when you create an [`AVURLAsset`](avurlasset.md) by passing a value for the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option.

## See Also

- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/duration)*