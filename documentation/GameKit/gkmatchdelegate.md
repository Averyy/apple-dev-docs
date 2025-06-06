# GKMatchDelegate

**Framework**: GameKit  
**Kind**: protocol

An object that receives connection status and data transmitted in a multiplayer game.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKMatchDelegate : NSObjectProtocol
```

## Topics

### Receiving Data from Other Players
- [func match(GKMatch, didReceive: Data, forRecipient: GKPlayer, fromRemotePlayer: GKPlayer)](gkmatchdelegate/match(_:didreceive:forrecipient:fromremoteplayer:).md)
  Processes the data sent from one player to another.
- [func match(GKMatch, didReceive: Data, fromRemotePlayer: GKPlayer)](gkmatchdelegate/match(_:didreceive:fromremoteplayer:).md)
  Processes the data sent from another player to the local player.
### Receiving State Notifications About Other Players
- [func match(GKMatch, player: GKPlayer, didChange: GKPlayerConnectionState)](gkmatchdelegate/match(_:player:didchange:)-8ohgr.md)
  Handles when players connect or disconnect from a match.
- [enum GKPlayerConnectionState](gkplayerconnectionstate.md)
  The possible states of a connection to a match.
### Handling Errors
- [func match(GKMatch, didFailWithError: (any Error)?)](gkmatchdelegate/match(_:didfailwitherror:).md)
  Handles the local player’s connection errors to a match.
### Reinviting a Player
- [func match(GKMatch, shouldReinviteDisconnectedPlayer: GKPlayer) -> Bool](gkmatchdelegate/match(_:shouldreinvitedisconnectedplayer:).md)
  Determines whether the local player should reinvite another player who disconnected from a two-player match.
### Deprecated Methods and Properties
- [func match(GKMatch, player: String, didChange: GKPlayerConnectionState)](gkmatchdelegate/match(_:player:didchange:)-4eo7p.md)
  Handles when a player connects or disconnects from a match.
- [func match(GKMatch, didReceive: Data, fromPlayer: String)](gkmatchdelegate/match(_:didreceive:fromplayer:).md)
  Handles when a player receives data in a match.
- [func match(GKMatch, shouldReinvitePlayer: String) -> Bool](gkmatchdelegate/match(_:shouldreinviteplayer:).md)
  Handles when a player disconnects from a two-player match.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any GKMatchDelegate)?](gkmatch/delegate.md)
  The delegate that handles communication between players in a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate)*