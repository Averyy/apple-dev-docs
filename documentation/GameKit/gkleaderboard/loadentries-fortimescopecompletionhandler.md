# loadEntries(for:timeScope:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Returns the scores for the local player and other players for the specified time period.

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
func loadEntries(for players: [GKPlayer], timeScope: GKLeaderboard.TimeScope) async throws -> (GKLeaderboard.Entry?, [GKLeaderboard.Entry])
```

## Mentions

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)

## Parameters

- `players`: The players whose scores this method returns.
- `timeScope`: Specifies the time period for the scores. This parameter is applicable to nonrecurring leaderboards only. For recurring leaderboards, pass   for this parameter.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:range:completionhandler:).md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.enum.md)
  Specifies the time period for filtering data.
- [GKLeaderboard.Entry](gkleaderboard/entry.md)
  Information about a single score by a player on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadentries(for:timescope:completionhandler:))*