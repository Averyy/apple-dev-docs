# showExistingMatches

**Framework**: GameKit  
**Kind**: property

A Boolean value that determines whether the view controller shows existing matches.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var showExistingMatches: Bool { get set }
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the view controller shows matches that are in progress or complete. If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the view controller only offers the ability to create new matches. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [init(matchRequest: GKMatchRequest)](gkturnbasedmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players to a turn-based game.
- [var matchmakingMode: GKMatchmakingMode](gkturnbasedmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/showexistingmatches)*