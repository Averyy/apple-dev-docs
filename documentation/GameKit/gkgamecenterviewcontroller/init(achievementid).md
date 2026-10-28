# init(achievementID:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that presents an achievement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(achievementID: String)
```

```objc
- (instancetype) initWithAchievementID:(NSString *) achievementID;
```

## Return Value

The initialized view controller.

## Parameters

- `achievementID`: The identifier for the achievement to display.

## See Also

### Configuring Game Center content
- [init(state: GKGameCenterViewControllerState)](./init%28state%29.md)
  Creates a view controller that presents the specified Game Center content.
- [enum GKGameCenterViewControllerState](../gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](./init%28leaderboard,playerscope%29.md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](./init%28leaderboardid,playerscope,timescope%29.md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(leaderboardSetID: String)](./init%28leaderboardsetid%29.md)
  Creates a view controller that presents a leaderboard set.
- [init(player: GKPlayer)](./init%28player%29.md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(achievementid:))*