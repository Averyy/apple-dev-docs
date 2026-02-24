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
- `timeScope`: Specifies the time period for the scores. This parameter is applicable to nonrecurring leaderboards only. For recurring leaderboards, pass [`GKLeaderboard.TimeScope.allTime`](gkleaderboard/timescope-swift.enum/alltime.md) for this parameter.
- `completionHandler`: A block that GameKit calls when this method loads the scores. The block receives the following parameters: - **localPlayerEntry**: The score for the local player, or `nil` if the player has no score.
- **entries**: The scores for the players during the specified time period, including the local player’s score if it exists.
- **error**: Describes an error if it occurs, or `nil` if the operation completes.

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