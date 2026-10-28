# playerIDs

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player identifiers for remote players in the match.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`players`](./players.md) property instead.

## Declaration

```swift
var playerIDs: [String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSString *> * playerIDs;
```

## Discussion

The `playerIDs` property initially includes the player identifiers for any remote players already connected to the match; the array may initially be empty. As each new player connects to the match, GameKit adds the player’s identifier to the array. GameKit doesn’t include the local player’s identifier in this array.

## See Also

### Related Documentation
- [var expectedPlayerCount: Int](./expectedplayercount.md)
  The remaining number of players invited but not yet connected to the match.
### Deprecated Methods and Properties
- [func chooseBestHostPlayer(completionHandler: (String?) -> Void)](./choosebesthostplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server match.
- [func send(Data, toPlayers: [String], with: GKMatch.SendDataMode) throws](./send%28_,toplayers,with%29.md)
  Transmits data to a list of connected players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/playerids)*