# minimumTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time value that indicates how closely playback follows the latest live stream content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var minimumTimeOffsetFromLive: CMTime { get }
```

#### Discussion

This property value is only valid when working with live streaming content. For non-live assets, this property value is [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Accessing duration and timing
- [var duration: CMTime](./duration.md)
  A time value that indicates the asset’s duration.
- [var providesPreciseDurationAndTiming: Bool](./providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/minimumtimeoffsetfromlive)*