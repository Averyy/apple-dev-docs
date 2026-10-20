# minimumTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A time value that indicates how closely playback follows the latest live stream content.

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
static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime> { get }
```

Available when `Root` inherits `AVAsset`.

#### Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

This property value is only valid when working with live streaming content. For non-live assets, this property value is [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Loading duration and timing
- [static var duration: AVAsyncProperty<Root, CMTime>](./duration.md)
  A time value that represents the duration of the asset.
- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](./providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/minimumtimeoffsetfromlive)*