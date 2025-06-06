# match(_:player:didChange:)

**Framework**: GameKit  
**Kind**: method

Handles when a player connects or disconnects from a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, player playerID: String, didChange state: GKPlayerConnectionState)
```

#### Discussion

Implement this method to be notified when players connect to or disconnect from the match.

## Parameters

- `match`: The match that the player is connected to.
- `playerID`: The identifier for the player whose state changed.
- `state`: The state the player moved to.

## See Also

- [func match(GKMatch, didReceive: Data, fromPlayer: String)](gkmatchdelegate/match(_:didreceive:fromplayer:).md)
  Handles when a player receives data in a match.
- [func match(GKMatch, shouldReinvitePlayer: String) -> Bool](gkmatchdelegate/match(_:shouldreinviteplayer:).md)
  Handles when a player disconnects from a two-player match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:player:didchange:)-4eo7p)*