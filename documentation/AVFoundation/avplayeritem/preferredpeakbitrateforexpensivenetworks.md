# preferredPeakBitRateForExpensiveNetworks

**Framework**: Avfoundation  
**Kind**: property

A limit of network bandwidth consumption by the item when connecting over expensive networks.

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
nonisolated
var preferredPeakBitRateForExpensiveNetworks: Double { get set }
```

#### Discussion

When this value is nonzero, the player attempts to limit item playback by the specified bit rate when streaming over an expensive network, such as a cellular data plan. If the system can’t reduce the bit rate to meet this value, it reduces it as much as possible while it continues to play the item.

> **Note**:  The value of the [`preferredPeakBitRate`](avplayeritem/preferredpeakbitrate.md) property applies unconditionally. This property value has no effect if this property value is less restrictive than the [`preferredPeakBitRate`](avplayeritem/preferredpeakbitrate.md) value.

## See Also

- [var preferredMaximumResolutionForExpensiveNetworks: CGSize](avplayeritem/preferredmaximumresolutionforexpensivenetworks.md)
  An upper limit on the resolution of video to download when connecting over expensive networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredpeakbitrateforexpensivenetworks)*