# init(leaderboardSetID:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

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
init(leaderboardSetID: String)
```

```objc
- (instancetype) initWithLeaderboardSetID:(NSString *) leaderboardSetID;
```

## Parameters

- `leaderboardSetID`: The identifier for the leaderboard set.

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
- [init(achievementID: String)](./init%28achievementid%29.md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](./init%28player%29.md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/init(leaderboardsetid:))*