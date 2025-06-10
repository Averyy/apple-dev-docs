# AVPlayer.NetworkResourcePriority

**Framework**: AVFoundation  
**Kind**: enum

This defines the network resource priority for a player.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum NetworkResourcePriority
```

## Topics

### Enumeration Cases
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum)*