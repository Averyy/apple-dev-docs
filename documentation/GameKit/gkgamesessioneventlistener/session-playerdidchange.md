# session(_:player:didChange:)

**Framework**: GameKit  
**Kind**: method

Tells the listener a player’s connection state has changed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, player: GKCloudPlayer, didChange newState: GKConnectionState)
```

## Parameters

- `session`: The game session affected by the connection state change.
- `player`: The player who’s connection state has changed.
- `newState`: The new connection state for the player.

## See Also

- [func session(GKGameSession, didAdd: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didadd:).md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, didRemove: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didremove:).md)
  Tells the listener a player left a game session.
- [enum GKConnectionState](gkconnectionstate.md)
  Possible connection states for a player


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:player:didchange:))*