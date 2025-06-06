# init(leaderboard:playerScope:)

**Framework**: GameKit  
**Kind**: init

Creates a view controller that presents a leaderboard with data for the specified players.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)
```

#### Return Value

The initialized view controller.

## Parameters

- `leaderboard`: The identifier for the leaderboard to display.
- `playerScope`: The type of players to display in the leaderboard.

## See Also

- [init(state: GKGameCenterViewControllerState)](gkgamecenterviewcontroller/init(state:).md)
  Creates a view controller that presents the specified Game Center content.
- [enum GKGameCenterViewControllerState](gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](gkgamecenterviewcontroller/init(leaderboardid:playerscope:timescope:).md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(leaderboardSetID: String)](gkgamecenterviewcontroller/init(leaderboardsetid:).md)
  Creates a view controller that presents a leaderboard set.
- [init(achievementID: String)](gkgamecenterviewcontroller/init(achievementid:).md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](gkgamecenterviewcontroller/init(player:).md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(leaderboard:playerscope:))*