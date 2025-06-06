# init(leaderboardSetID:)

**Framework**: GameKit  
**Kind**: init

Creates a view controller that presents a leaderboard set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
init(leaderboardSetID: String)
```

## Parameters

- `leaderboardSetID`: The identifier for the leaderboard set.

## See Also

- [init(state: GKGameCenterViewControllerState)](gkgamecenterviewcontroller/init(state:).md)
  Creates a view controller that presents the specified Game Center content.
- [enum GKGameCenterViewControllerState](gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](gkgamecenterviewcontroller/init(leaderboard:playerscope:).md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](gkgamecenterviewcontroller/init(leaderboardid:playerscope:timescope:).md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(achievementID: String)](gkgamecenterviewcontroller/init(achievementid:).md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](gkgamecenterviewcontroller/init(player:).md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(leaderboardsetid:))*