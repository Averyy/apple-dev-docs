# session(_:didAdd:)

**Framework**: GameKit  
**Kind**: method

Tells the listener a new player has been added to a game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: GKGameSession, didAdd player: GKCloudPlayer)
```

## Parameters

- `session`: The game session that added a player.
- `player`: The player that was added to the session.

## See Also

- [func session(GKGameSession, didRemove: GKCloudPlayer)](gkgamesessioneventlistener/session(_:didremove:).md)
  Tells the listener a player left a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](gkgamesessioneventlistener/session(_:player:didchange:).md)
  Tells the listener a player’s connection state has changed.
- [enum GKConnectionState](gkconnectionstate.md)
  Possible connection states for a player


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didadd:))*