# GKLeaderboard.TimeScope

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GKLeaderboardTimeScope : NSInteger;
```

## Topics

### Constants
- [GKLeaderboard.TimeScope.today](./timescope-swift.enum/today.md)
  Loads data for the past 24 hours.
- [GKLeaderboard.TimeScope.week](./timescope-swift.enum/week.md)
  Loads data for the past week.
- [GKLeaderboard.TimeScope.allTime](./timescope-swift.enum/alltime.md)
  Loads a player’s best score.
### Initializers
- [init?(rawValue: Int)](./timescope-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading Scores
- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](./loadentries%28for,timescope,range,completionhandler%29.md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](./loadentries%28for,timescope,completionhandler%29.md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](./playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.Entry](./entry.md)
  Information about a single score by a player on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/timescope-swift.enum)*