# init(leaderboardID:playerScope:timeScope:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that presents a leaderboard with data from the specified players and time period.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)
```

```objc
- (instancetype) initWithLeaderboardID:(NSString *) leaderboardID playerScope:(GKLeaderboardPlayerScope) playerScope timeScope:(GKLeaderboardTimeScope) timeScope;
```

## Return Value

The initialized view controller.

## Parameters

- `leaderboardID`: The identifier for the leaderboard to display.
- `playerScope`: The type of players to display in the leaderboard.
- `timeScope`: The time period for the data to display in a classic leaderboard.

  For recurring leaderboards, this method ignores the time scope parameter and displays the data for the current occurrence instead.

## See Also

### Configuring Game Center content
- [init(state: GKGameCenterViewControllerState)](./init%28state%29.md)
  Creates a view controller that presents the specified Game Center content.
- [enum GKGameCenterViewControllerState](../gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](./init%28leaderboard,playerscope%29.md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardSetID: String)](./init%28leaderboardsetid%29.md)
  Creates a view controller that presents a leaderboard set.
- [init(achievementID: String)](./init%28achievementid%29.md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](./init%28player%29.md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(leaderboardid:playerscope:timescope:))*