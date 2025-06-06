# matchmakingMode

**Framework**: GameKit  
**Kind**: property

The mode that a multiplayer game uses to find players.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var matchmakingMode: GKMatchmakingMode { get set }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

This method throws an exception if you set the mode to a value that isn’t possible due to restrictions.

## See Also

- [init(matchRequest: GKMatchRequest)](gkturnbasedmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players to a turn-based game.
- [var showExistingMatches: Bool](gkturnbasedmatchmakerviewcontroller/showexistingmatches.md)
  A Boolean value that determines whether the view controller shows existing matches.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/matchmakingmode)*