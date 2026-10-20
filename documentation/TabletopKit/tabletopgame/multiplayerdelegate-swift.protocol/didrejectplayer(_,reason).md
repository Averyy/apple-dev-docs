# didRejectPlayer(_:reason:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A player that tried to join was rejected or a player that previously joined our game was ejected.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func didRejectPlayer(_ playerID: PlayerIdentifier, reason: any Error)
```

## See Also

### Handling errors
- [func multiplayerSessionFailed(reason: any Error)](./multiplayersessionfailed%28reason%29.md)
  We failed to start or join a new multiplayer session or had to terminate a previously started multiplayer session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/multiplayerdelegate-swift.protocol/didrejectplayer(_:reason:))*