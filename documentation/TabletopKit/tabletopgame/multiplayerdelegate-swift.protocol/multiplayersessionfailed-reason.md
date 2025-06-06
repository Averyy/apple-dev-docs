# multiplayerSessionFailed(reason:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

We failed to start or join a new multiplayer session or had to terminate a previously started multiplayer session.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func multiplayerSessionFailed(reason: any Error)
```

## See Also

- [func didRejectPlayer(PlayerIdentifier, reason: any Error)](tabletopgame/multiplayerdelegate-swift.protocol/didrejectplayer(_:reason:).md)
  A player that tried to join was rejected or a player that previously joined our game was ejected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/multiplayerdelegate-swift.protocol/multiplayersessionfailed(reason:))*