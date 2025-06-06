# GKLeaderboard.TimeScope

**Framework**: GameKit  
**Kind**: enum

Specifies the time period for filtering data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum TimeScope
```

## Topics

### Constants
- [GKLeaderboard.TimeScope.today](gkleaderboard/timescope-swift.enum/today.md)
  Loads data for the past 24 hours.
- [GKLeaderboard.TimeScope.week](gkleaderboard/timescope-swift.enum/week.md)
  Loads data for the past week.
- [GKLeaderboard.TimeScope.allTime](gkleaderboard/timescope-swift.enum/alltime.md)
  Loads a player’s best score.
### Initializers
- [init?(rawValue: Int)](gkleaderboard/timescope-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:range:completionhandler:).md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:completionhandler:).md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.Entry](gkleaderboard/entry.md)
  Information about a single score by a player on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/timescope-swift.enum)*