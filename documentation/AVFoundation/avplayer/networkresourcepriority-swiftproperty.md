# networkResourcePriority

**Framework**: AVFoundation  
**Kind**: property

Indicates the priority of this player for network bandwidth resource distribution.

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
@MainActor
var networkResourcePriority: AVPlayer.NetworkResourcePriority { get set }
```

#### Discussion

This value determines the priority of the player during network resource allocation among all other players within the same application process. The default value for this is AVPlayerNetworkResourcePriorityDefault.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/networkresourcepriority-swift.property)*