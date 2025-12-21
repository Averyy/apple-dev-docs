# AVPlayer.NetworkResourcePriority

**Framework**: AVFoundation  
**Kind**: enum

This defines the network resource priority for a player.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum NetworkResourcePriority
```

## Topics

### Priorities
- [AVPlayer.NetworkResourcePriority.default](avplayer/networkresourcepriority-swift.enum/default.md)
  The default priority level given to a player for loading network resources. Use this when the player requires an optimal level of network resources and streaming in high-quality resolution is ideal. Players with AVPlayerNetworkResourcePriorityHigh will take precedence over this player. This player will take precedence over players with AVPlayerNetworkResourcePriorityLow.
- [AVPlayer.NetworkResourcePriority.high](avplayer/networkresourcepriority-swift.enum/high.md)
  Indicates a high priority level for loading network resources. Use this when the player requires a high level of network resources and streaming in high-quality resolution is crucial. This player will take precedence over other lower priority players.
- [AVPlayer.NetworkResourcePriority.low](avplayer/networkresourcepriority-swift.enum/low.md)
  Indicates a low priority level for loading network resources. Use this when the player requires minimal network bandwidth and streaming in high-quality resolution is not crucial. Other players with higher priority will take precedence over this player.
### Initializers
- [init?(rawValue: Int)](avplayer/networkresourcepriority-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var networkResourcePriority: AVPlayer.NetworkResourcePriority](avplayer/networkresourcepriority-swift.property.md)
  Indicates the priority of this player for network bandwidth resource distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum)*