# GKConnectionState

**Framework**: GameKit  
**Kind**: enum

Possible connection states for a player

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKConnectionState
```

## Topics

### Constants
- [GKConnectionState.connected](gkconnectionstate/connected.md)
  The player is connected to the game session.
- [GKConnectionState.notConnected](gkconnectionstate/notconnected.md)
  The player is not connected to the game session.
### Initializers
- [init?(rawValue: Int)](gkconnectionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func session(GKGameSession, didAdd: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didadd:).md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, didRemove: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didremove:).md)
  Tells the listener a player left a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](gkgamesessioneventlistener/session(_:player:didchange:).md)
  Tells the listener a player’s connection state has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkconnectionstate)*