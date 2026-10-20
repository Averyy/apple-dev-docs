# session(_:player:didChange:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the listener a player’s connection state has changed.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func session(_ session: GKGameSession, player: GKCloudPlayer, didChange newState: GKConnectionState)
```

```objc
- (void) session:(GKGameSession *) session player:(GKCloudPlayer *) player didChangeConnectionState:(GKConnectionState) newState;
```

## Parameters

- `session`: The game session affected by the connection state change.
- `player`: The player who’s connection state has changed.
- `newState`: The new connection state for the player.

## See Also

### Changing Player Status
- [func session(GKGameSession, didAdd: GKCloudPlayer)](./session%28_,didadd%29.md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, didRemove: GKCloudPlayer)](./session%28_,didremove%29.md)
  Tells the listener a player left a game session.
- [enum GKConnectionState](../gkconnectionstate.md)
  Possible connection states for a player


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:player:didchange:))*