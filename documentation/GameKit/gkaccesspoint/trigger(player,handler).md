# trigger(player:handler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Displays the Game Center dashboard in a state that shows a player profile.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func trigger(player: GKPlayer, handler: (() -> Void)? = nil)
```

```objc
- (void) triggerAccessPointWithPlayer:(GKPlayer *) player handler:(void (^)()) handler;
```

## Parameters

- `player`: The player to show in the dashboard.
- `handler`: The block that GameKit calls after it displays the dashboard.

## See Also

### Managing the access point
- [var isFocused: Bool](./isfocused.md)
  A Boolean value that indicates whether the access point is in focus on tvOS.
- [func trigger(handler: () -> Void)](./trigger%28handler%29.md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(state: GKGameCenterViewControllerState, handler: () -> Void)](./trigger%28state,handler%29.md)
  Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.
- [func trigger(achievementID: String, handler: (() -> Void)?)](./trigger%28achievementid,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific achievement.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](./trigger%28leaderboardid,playerscope,timescope,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](./trigger%28leaderboardsetid,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(player:handler:))*