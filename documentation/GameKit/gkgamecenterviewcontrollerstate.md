# GKGameCenterViewControllerState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The type of content for the view controller to present.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum GKGameCenterViewControllerState
```

```c
enum GKGameCenterViewControllerState : NSInteger;
```

## Topics

### States
- [GKGameCenterViewControllerState.default](./gkgamecenterviewcontrollerstate/default.md)
  The view controller should present the default screen.
- [GKGameCenterViewControllerState.leaderboards](./gkgamecenterviewcontrollerstate/leaderboards.md)
  The view controller should present leaderboard sets or leaderboards if there are no sets.
- [GKGameCenterViewControllerState.achievements](./gkgamecenterviewcontrollerstate/achievements.md)
  The view controller should present a list of achievements.
- [GKGameCenterViewControllerState.challenges](./gkgamecenterviewcontrollerstate/challenges.md)
  The view controller should present a list of challenges.
- [GKGameCenterViewControllerState.localPlayerProfile](./gkgamecenterviewcontrollerstate/localplayerprofile.md)
  The view controller should present the local player’s profile.
- [GKGameCenterViewControllerState.dashboard](./gkgamecenterviewcontrollerstate/dashboard.md)
  The view controller should present the dashboard.
- [GKGameCenterViewControllerState.localPlayerFriendsList](./gkgamecenterviewcontrollerstate/localplayerfriendslist.md)
  The view controller should present the friends list.
### Initializers
- [init?(rawValue: Int)](./gkgamecenterviewcontrollerstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring Game Center content
- [init(state: GKGameCenterViewControllerState)](./gkgamecenterviewcontroller/init%28state%29.md)
  Creates a view controller that presents the specified Game Center content.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](./gkgamecenterviewcontroller/init%28leaderboard,playerscope%29.md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](./gkgamecenterviewcontroller/init%28leaderboardid,playerscope,timescope%29.md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(leaderboardSetID: String)](./gkgamecenterviewcontroller/init%28leaderboardsetid%29.md)
  Creates a view controller that presents a leaderboard set.
- [init(achievementID: String)](./gkgamecenterviewcontroller/init%28achievementid%29.md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](./gkgamecenterviewcontroller/init%28player%29.md)
  Creates a view controller that presents a player’s Game Center profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate)*