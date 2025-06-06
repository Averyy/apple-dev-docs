# match(_:player:didChange:)

**Framework**: GameKit  
**Kind**: method

Handles when players connect or disconnect from a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, player: GKPlayer, didChange state: GKPlayerConnectionState)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)

#### Discussion

If the match’s [`expectedPlayerCount`](gkmatch/expectedplayercount.md) property is `0` when GameKit invokes this method, you can start the game. If two or more players join the match, you can begin data and voice communication.

## Parameters

- `match`: The match joined by the player.
- `player`: The player whose state changed.
- `state`: The state of the player in the match.

## See Also

- [enum GKPlayerConnectionState](gkplayerconnectionstate.md)
  The possible states of a connection to a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:player:didchange:)-8ohgr)*