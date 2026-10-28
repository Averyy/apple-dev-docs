# match(_:shouldReinvitePlayer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when a player disconnects from a two-player match.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool
```

```objc
- (BOOL) match:(GKMatch *) match shouldReinvitePlayer:(NSString *) playerID;
```

## Return Value

Your game should return [`true`](../../Swift/true.md) if it wants GameKit to attempt to reconnect the player, [`false`](../../Swift/false.md) if it wants to terminate the match.

## Discussion

Occasionally, players may get disconnected from a match. If your game implements this method in the match delegate and the match only contains two players, GameKit calls this method after a player gets disconnected. If your delegate allows GameKit to reconnect to the other player, it reconnects the other player. Your [`match(_:player:didChange:)`](./match%28_,player,didchange%29-4eo7p.md) method is called when the other player is reconnected.

## Parameters

- `match`: The match that lost the player.
- `playerID`: The identifier for the player whose connection failed.

## See Also

### Deprecated Methods and Properties
- [func match(GKMatch, player: String, didChange: GKPlayerConnectionState)](./match%28_,player,didchange%29-4eo7p.md)
  Handles when a player connects or disconnects from a match.
- [func match(GKMatch, didReceive: Data, fromPlayer: String)](./match%28_,didreceive,fromplayer%29.md)
  Handles when a player receives data in a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:shouldreinviteplayer:))*