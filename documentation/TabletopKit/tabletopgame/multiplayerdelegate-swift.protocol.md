# TabletopGame.MultiplayerDelegate

**Framework**: TabletopKit  
**Kind**: protocol  
**Role**: Protocol

An object that handles players joining multiplayer games.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol MultiplayerDelegate : AnyObject
```

## Topics

### Joining games
- [func joinAccepted()](./multiplayerdelegate-swift.protocol/joinaccepted%28%29.md)
  We tried to join a game and got accepted
- [func playerJoined(PlayerIdentifier)](./multiplayerdelegate-swift.protocol/playerjoined%28_%29.md)
  A player joined our multiplayer session
### Handling errors
- [func didRejectPlayer(PlayerIdentifier, reason: any Error)](./multiplayerdelegate-swift.protocol/didrejectplayer%28_,reason%29.md)
  A player that tried to join was rejected or a player that previously joined our game was ejected.
- [func multiplayerSessionFailed(reason: any Error)](./multiplayerdelegate-swift.protocol/multiplayersessionfailed%28reason%29.md)
  We failed to start or join a new multiplayer session or had to terminate a previously started multiplayer session.

## See Also

### Supporting multiple players
- [func attachNetworkCoordinator(some TabletopNetworkSessionCoordinator)](./attachnetworkcoordinator%28_%29.md)
- [func detachNetworkCoordinator()](./detachnetworkcoordinator%28%29.md)
- [var multiplayerDelegate: (any TabletopGame.MultiplayerDelegate)?](./multiplayerdelegate-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/multiplayerdelegate-swift.protocol)*