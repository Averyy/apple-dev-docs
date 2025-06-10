# GKLeaderboard.LeaderboardType

**Framework**: GameKit  
**Kind**: enum

Specifies whether a leaderboard is recurring.

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
enum LeaderboardType
```

## Topics

### Constants
- [GKLeaderboard.LeaderboardType.classic](gkleaderboard/leaderboardtype/classic.md)
  A leaderboard that never expires, showing all-time rankings of all players.
- [GKLeaderboard.LeaderboardType.recurring](gkleaderboard/leaderboardtype/recurring.md)
  A leaderboard that recurs, allowing players a fresh start to compete and earn higher ranks in each ocurrence.
### Initializers
- [init?(rawValue: Int)](gkleaderboard/leaderboardtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var baseLeaderboardID: String](gkleaderboard/baseleaderboardid.md)
  The ID that Game Center uses to identify this leaderboard.
- [var title: String?](gkleaderboard/title.md)
  The localized title for the leaderboard.
- [var type: GKLeaderboard.LeaderboardType](gkleaderboard/type.md)
  The type of leaderboard, classic or recurring.
- [var groupIdentifier: String?](gkleaderboard/groupidentifier.md)
  The identifier for the group the leaderboard belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/leaderboardtype)*