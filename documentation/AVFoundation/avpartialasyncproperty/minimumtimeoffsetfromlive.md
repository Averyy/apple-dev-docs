# minimumTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates how closely playback follows the latest live stream content.

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
static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

This property value is only valid when working with live streaming content. For non-live assets, this property value is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid).

## See Also

- [static var duration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/duration.md)
  A time value that represents the duration of the asset.
- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/minimumtimeoffsetfromlive)*