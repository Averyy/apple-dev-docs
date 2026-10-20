# GKLeaderboard.LeaderboardType

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GKLeaderboardType : NSInteger;
```

## Topics

### Constants
- [GKLeaderboard.LeaderboardType.classic](./leaderboardtype/classic.md)
  A leaderboard that never expires, showing all-time rankings of all players.
- [GKLeaderboard.LeaderboardType.recurring](./leaderboardtype/recurring.md)
  A leaderboard that recurs, allowing players a fresh start to compete and earn higher ranks in each ocurrence.
### Initializers
- [init?(rawValue: Int)](./leaderboardtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Identifier and Type Properties
- [var baseLeaderboardID: String](./baseleaderboardid.md)
  The ID that Game Center uses to identify this leaderboard.
- [var title: String?](./title.md)
  The localized title for the leaderboard.
- [var type: GKLeaderboard.LeaderboardType](./type.md)
  The type of leaderboard, classic or recurring.
- [var groupIdentifier: String?](./groupidentifier.md)
  The identifier for the group the leaderboard belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/leaderboardtype)*