# networkResourcePriority

**Framework**: AVFoundation  
**Kind**: property

Indicates the priority of this player for network bandwidth resource distribution.

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
@MainActor
var networkResourcePriority: AVPlayer.NetworkResourcePriority { get set }
```

#### Discussion

This value determines the priority of the player during network resource allocation among all other players within the same application process. The default value for this is AVPlayerNetworkResourcePriorityDefault.

## See Also

- [AVPlayer.NetworkResourcePriority](avplayer/networkresourcepriority-swift.enum.md)
  This defines the network resource priority for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.property)*