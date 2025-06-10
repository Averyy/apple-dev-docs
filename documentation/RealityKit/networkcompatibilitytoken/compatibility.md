# NetworkCompatibilityToken.Compatibility

**Framework**: RealityKit  
**Kind**: enum

Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum Compatibility
```

## Topics

### Compatibility indicators
- [NetworkCompatibilityToken.Compatibility.compatible](networkcompatibilitytoken/compatibility/compatible.md)
  An indication that the compared devices are running compatible versions of RealityKit.
- [NetworkCompatibilityToken.Compatibility.sessionProtocolVersionMismatch](networkcompatibilitytoken/compatibility/sessionprotocolversionmismatch.md)
  An indication that two peers running incompatible versions of RealityKit can’t sync.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Loading remote assets in multiplayer apps](loading-remote-assets.md)
  Ensure assets load on all connected peers before using them.
- [class MultipeerConnectivityService](multipeerconnectivityservice.md)
  A service that provides scene synchronization among all peers in a multipeer connectivity session.
- [class NetworkCompatibilityToken](networkcompatibilitytoken.md)
  An opaque token used to check the networking compatibility between two peers in a multipeer connection.
- [protocol TransientComponent](transientcomponent.md)
  An interface for components that aren’t saved to file or cloned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibility)*