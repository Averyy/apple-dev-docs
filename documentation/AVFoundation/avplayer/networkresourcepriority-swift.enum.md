# AVPlayer.NetworkResourcePriority

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVPlayerNetworkResourcePriority : NSInteger;
```

## Topics

### Priorities
- [AVPlayer.NetworkResourcePriority.default](./networkresourcepriority-swift.enum/default.md)
  The default priority level given to a player for loading network resources. Use this when the player requires an optimal level of network resources and streaming in high-quality resolution is ideal. Players with AVPlayerNetworkResourcePriorityHigh will take precedence over this player. This player will take precedence over players with AVPlayerNetworkResourcePriorityLow.
- [AVPlayer.NetworkResourcePriority.high](./networkresourcepriority-swift.enum/high.md)
  Indicates a high priority level for loading network resources. Use this when the player requires a high level of network resources and streaming in high-quality resolution is crucial. This player will take precedence over other lower priority players.
- [AVPlayer.NetworkResourcePriority.low](./networkresourcepriority-swift.enum/low.md)
  Indicates a low priority level for loading network resources. Use this when the player requires minimal network bandwidth and streaming in high-quality resolution is not crucial. Other players with higher priority will take precedence over this player.
### Initializers
- [init?(rawValue: Int)](./networkresourcepriority-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the network resource priority
- [var networkResourcePriority: AVPlayer.NetworkResourcePriority](./networkresourcepriority-swift.property.md)
  Indicates the priority of this player for network bandwidth resource distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.enum)*