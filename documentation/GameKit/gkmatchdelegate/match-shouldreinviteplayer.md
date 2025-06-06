# match(_:shouldReinvitePlayer:)

**Framework**: GameKit  
**Kind**: method

Handles when a player disconnects from a two-player match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool
```

#### Return Value

Your game should return [`true`](https://developer.apple.com/documentation/swift/true) if it wants GameKit to attempt to reconnect the player, [`false`](https://developer.apple.com/documentation/swift/false) if it wants to terminate the match.

#### Discussion

Occasionally, players may get disconnected from a match. If your game implements this method in the match delegate and the match only contains two players, GameKit calls this method after a player gets disconnected. If your delegate allows GameKit to reconnect to the other player, it reconnects the other player. Your [`match(_:player:didChange:)`](gkmatchdelegate/match(_:player:didchange:)-4eo7p.md) method is called when the other player is reconnected.

## Parameters

- `match`: The match that lost the player.
- `playerID`: The identifier for the player whose connection failed.

## See Also

- [func match(GKMatch, player: String, didChange: GKPlayerConnectionState)](gkmatchdelegate/match(_:player:didchange:)-4eo7p.md)
  Handles when a player connects or disconnects from a match.
- [func match(GKMatch, didReceive: Data, fromPlayer: String)](gkmatchdelegate/match(_:didreceive:fromplayer:).md)
  Handles when a player receives data in a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:shouldreinviteplayer:))*