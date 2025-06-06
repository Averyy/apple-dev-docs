# match(_:didReceive:forRecipient:fromRemotePlayer:)

**Framework**: GameKit  
**Kind**: method

Processes the data sent from one player to another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, didReceive data: Data, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer)
```

#### Discussion

Your game defines its own format for data packets it transmits and receives over the network.

> ❗ **Important**:  You need to treat data you receive from other players as  data. Be sure to validate the data you receive from the match and write your code carefully to avoid security vulnerabilities.

 You need to treat data you receive from other players as  data. Be sure to validate the data you receive from the match and write your code carefully to avoid security vulnerabilities.

## Parameters

- `match`: The match associated with the data.
- `data`: The data sent by the player.
- `recipient`: The player who receives the data.
- `player`: The player who sends the data.

## See Also

- [func match(GKMatch, didReceive: Data, fromRemotePlayer: GKPlayer)](gkmatchdelegate/match(_:didreceive:fromremoteplayer:).md)
  Processes the data sent from another player to the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:didreceive:forrecipient:fromremoteplayer:))*