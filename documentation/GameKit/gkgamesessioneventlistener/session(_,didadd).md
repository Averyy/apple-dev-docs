# session(_:didAdd:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Tells the listener a new player has been added to a game session.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func session(_ session: GKGameSession, didAdd player: GKCloudPlayer)
```

```objc
- (void) session:(GKGameSession *) session didAddPlayer:(GKCloudPlayer *) player;
```

## Parameters

- `session`: The game session that added a player.
- `player`: The player that was added to the session.

## See Also

### Changing Player Status
- [func session(GKGameSession, didRemove: GKCloudPlayer)](./session%28_,didremove%29.md)
  Tells the listener a player left a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](./session%28_,player,didchange%29.md)
  Tells the listener a player’s connection state has changed.
- [enum GKConnectionState](../gkconnectionstate.md)
  Possible connection states for a player


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/session(_:didadd:))*