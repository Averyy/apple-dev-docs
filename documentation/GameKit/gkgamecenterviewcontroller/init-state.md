# init(state:)

**Framework**: GameKit  
**Kind**: init

Creates a view controller that presents the specified Game Center content.

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
init(state: GKGameCenterViewControllerState)
```

## Mentions

- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)

#### Return Value

The initialized view controller.

## Parameters

- `state`: The type of content to present.

## See Also

- [enum GKGameCenterViewControllerState](gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](gkgamecenterviewcontroller/init(leaderboard:playerscope:).md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](gkgamecenterviewcontroller/init(leaderboardid:playerscope:timescope:).md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(leaderboardSetID: String)](gkgamecenterviewcontroller/init(leaderboardsetid:).md)
  Creates a view controller that presents a leaderboard set.
- [init(achievementID: String)](gkgamecenterviewcontroller/init(achievementid:).md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](gkgamecenterviewcontroller/init(player:).md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(state:))*