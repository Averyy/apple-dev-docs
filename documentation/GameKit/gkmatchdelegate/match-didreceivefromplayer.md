# match(_:didReceive:fromPlayer:)

**Framework**: GameKit  
**Kind**: method

Handles when a player receives data in a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, didReceive data: Data, fromPlayer playerID: String)
```

#### Discussion

You define your own format for data packets that you transmit and receive over the network.

> ❗ **Important**:  You need to treat data you receive from other players as  data. Be sure to validate the data you receive from the match and write your code carefully to avoid security vulnerabilities.

 You need to treat data you receive from other players as  data. Be sure to validate the data you receive from the match and write your code carefully to avoid security vulnerabilities.

## Parameters

- `match`: The match that received the data.
- `data`: The bytes sent by the player.
- `playerID`: The string identifier for the player that sent the data.

## See Also

- [func match(GKMatch, player: String, didChange: GKPlayerConnectionState)](gkmatchdelegate/match(_:player:didchange:)-4eo7p.md)
  Handles when a player connects or disconnects from a match.
- [func match(GKMatch, shouldReinvitePlayer: String) -> Bool](gkmatchdelegate/match(_:shouldreinviteplayer:).md)
  Handles when a player disconnects from a two-player match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:didreceive:fromplayer:))*