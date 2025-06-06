# session(_:didRemove:)

**Framework**: GameKit  
**Kind**: method

Tells the listener a player left a game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, didRemove player: GKCloudPlayer)
```

## Parameters

- `session`: The game session the player left.
- `player`: The player that left the game session.

## See Also

- [func session(GKGameSession, didAdd: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didadd:).md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](gkgamesessioneventlistener/session(_:player:didchange:).md)
  Tells the listener a player’s connection state has changed.
- [enum GKConnectionState](gkconnectionstate.md)
  Possible connection states for a player


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didremove:))*