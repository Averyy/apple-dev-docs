# playerIDs

**Framework**: GameKit  
**Kind**: property

The player identifiers for remote players in the match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
var playerIDs: [String]? { get }
```

#### Discussion

The `playerIDs` property initially includes the player identifiers for any remote players already connected to the match; the array may initially be empty. As each new player connects to the match, GameKit adds the player’s identifier to the array. GameKit doesn’t include the local player’s identifier in this array.

## See Also

- [var expectedPlayerCount: Int](gkmatch/expectedplayercount.md)
  The remaining number of players invited but not yet connected to the match.
- [func chooseBestHostPlayer(completionHandler: (String?) -> Void)](gkmatch/choosebesthostplayer(completionhandler:).md)
  Determines the best player in the game to act as the server for a client-server match.
- [func send(Data, toPlayers: [String], with: GKMatch.SendDataMode) throws](gkmatch/send(_:toplayers:with:).md)
  Transmits data to a list of connected players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/playerids)*