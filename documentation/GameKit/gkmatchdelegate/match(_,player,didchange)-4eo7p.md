# match(_:player:didChange:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when a player connects or disconnects from a match.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func match(_ match: GKMatch, player playerID: String, didChange state: GKPlayerConnectionState)
```

```objc
- (void) match:(GKMatch *) match player:(NSString *) playerID didChangeState:(GKPlayerConnectionState) state;
```

#### Discussion

Implement this method to be notified when players connect to or disconnect from the match.

## Parameters

- `match`: The match that the player is connected to.
- `playerID`: The identifier for the player whose state changed.
- `state`: The state the player moved to.

## See Also

### Deprecated Methods and Properties
- [func match(GKMatch, didReceive: Data, fromPlayer: String)](./match%28_,didreceive,fromplayer%29.md)
  Handles when a player receives data in a match.
- [func match(GKMatch, shouldReinvitePlayer: String) -> Bool](./match%28_,shouldreinviteplayer%29.md)
  Handles when a player disconnects from a two-player match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:player:didchange:)-4eo7p)*