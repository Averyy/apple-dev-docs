# GKLeaderboard.PlayerScope

**Framework**: GameKit  
**Kind**: enum

Specifies the type of players for filtering data.

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
enum PlayerScope
```

## Topics

### Constants
- [GKLeaderboard.PlayerScope.global](gkleaderboard/playerscope-swift.enum/global.md)
  Loads data for all players of the game.
- [GKLeaderboard.PlayerScope.friendsOnly](gkleaderboard/playerscope-swift.enum/friendsonly.md)
  Loads only data for friends of the local player.
### Initializers
- [init?(rawValue: Int)](gkleaderboard/playerscope-swift.enum/init(rawvalue:).md)

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
- [GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.enum.md)
  Specifies the time period for filtering data.
- [GKLeaderboard.Entry](gkleaderboard/entry.md)
  Information about a single score by a player on a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/playerscope-swift.enum)*