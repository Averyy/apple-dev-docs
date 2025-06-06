# providesPreciseDurationAndTiming

**Framework**: Avfoundation  
**Kind**: property

A Boolean value that indicates whether the asset provides precise duration and timing.

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
static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

This property value is [`true`](https://developer.apple.com/documentation/swift/true) if you initialized the asset with the [`AVURLAssetPreferPreciseDurationAndTimingKey`](avurlassetpreferprecisedurationandtimingkey.md) initialization option, otherwise it’s [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  If calculating precise duration and timing isn’t possible for the media resources that the URL references, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), even if you requested otherwise.

## See Also

- [static var duration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/duration.md)
  A time value that represents the duration of the asset.
- [static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/providesprecisedurationandtiming)*