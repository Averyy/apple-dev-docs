# TabletopGame.MultiplayerDelegate

**Framework**: TabletopKit  
**Kind**: protocol

An object that handles players joining multiplayer games.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol MultiplayerDelegate : AnyObject
```

## Topics

### Joining games
- [func joinAccepted()](tabletopgame/multiplayerdelegate-swift.protocol/joinaccepted.md)
  We tried to join a game and got accepted
- [func playerJoined(PlayerIdentifier)](tabletopgame/multiplayerdelegate-swift.protocol/playerjoined(_:).md)
  A player joined our multiplayer session
### Handling errors
- [func didRejectPlayer(PlayerIdentifier, reason: any Error)](tabletopgame/multiplayerdelegate-swift.protocol/didrejectplayer(_:reason:).md)
  A player that tried to join was rejected or a player that previously joined our game was ejected.
- [func multiplayerSessionFailed(reason: any Error)](tabletopgame/multiplayerdelegate-swift.protocol/multiplayersessionfailed(reason:).md)
  We failed to start or join a new multiplayer session or had to terminate a previously started multiplayer session.

## See Also

- [func attachNetworkCoordinator(some TabletopNetworkSessionCoordinator)](tabletopgame/attachnetworkcoordinator(_:).md)
- [func detachNetworkCoordinator()](tabletopgame/detachnetworkcoordinator.md)
- [var multiplayerDelegate: (any TabletopGame.MultiplayerDelegate)?](tabletopgame/multiplayerdelegate-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/multiplayerdelegate-swift.protocol)*