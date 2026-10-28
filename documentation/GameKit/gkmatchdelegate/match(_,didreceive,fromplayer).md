# match(_:didReceive:fromPlayer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when a player receives data in a match.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func match(_ match: GKMatch, didReceive data: Data, fromPlayer playerID: String)
```

```objc
- (void) match:(GKMatch *) match didReceiveData:(NSData *) data fromPlayer:(NSString *) playerID;
```

## Discussion

You define your own format for data packets that you transmit and receive over the network.

> ❗ **Important**:  You need to treat data you receive from other players as *untrusted* data. Be sure to validate the data you receive from the match and write your code carefully to avoid security vulnerabilities.

## Parameters

- `match`: The match that received the data.
- `data`: The bytes sent by the player.
- `playerID`: The string identifier for the player that sent the data.

## See Also

### Deprecated Methods and Properties
- [func match(GKMatch, player: String, didChange: GKPlayerConnectionState)](./match%28_,player,didchange%29-4eo7p.md)
  Handles when a player connects or disconnects from a match.
- [func match(GKMatch, shouldReinvitePlayer: String) -> Bool](./match%28_,shouldreinviteplayer%29.md)
  Handles when a player disconnects from a two-player match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:didreceive:fromplayer:))*