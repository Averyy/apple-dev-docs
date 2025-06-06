# loadEntries(for:timeScope:range:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Returns the scores for the local player and other players for the specified type of player, time period, and ranks.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func loadEntries(for playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange) async throws -> (GKLeaderboard.Entry?, [GKLeaderboard.Entry], Int)
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

#### Discussion

GameKit uses the following algorithm to fetch [`GKLeaderboard`](gkleaderboard.md) scores:

1. Begins with the set of all possible scores for the leaderboard.
2. Discards any scores that don’t match the `playerScope` and `timeScope` properties.
3. For each player, keeps the best score that player earns and discards the rest.
4. Sorts the scores from best to worst.
5. Uses the range property to determine which scores return.

## Parameters

- `playerScope`: Specifies whether to get scores from friends or all players.
- `timeScope`: Specifies the time period for the scores. This parameter is applicable to nonrecurring leaderboards only. For recurring leaderboards, pass   for this parameter.
- `range`: Specifies the range of ranks to use for getting the scores. The difference between the minimum rank and maximum rank must not exceed  .
- `completionHandler`: The block receives the following parameters:

## See Also

- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:completionhandler:).md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.enum.md)
  Specifies the time period for filtering data.
- [GKLeaderboard.Entry](gkleaderboard/entry.md)
  Information about a single score by a player on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadentries(for:timescope:range:completionhandler:))*