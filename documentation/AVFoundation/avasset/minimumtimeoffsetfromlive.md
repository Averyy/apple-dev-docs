# minimumTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time value that indicates how closely playback follows the latest live stream content.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`minimumTimeOffsetFromLive`](../avpartialasyncproperty/minimumtimeoffsetfromlive.md) asynchronously instead.

## Declaration

```swift
var minimumTimeOffsetFromLive: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime minimumTimeOffsetFromLive;
```

## Discussion

This property value is only valid when working with live streaming content. For non-live assets, this property value is [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Accessing duration and timing
- [duration](./duration.md)
  A time value that indicates the asset’s duration.
- [providesPreciseDurationAndTiming](./providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/minimumtimeoffsetfromlive)*