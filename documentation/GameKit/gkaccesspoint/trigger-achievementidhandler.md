# trigger(achievementID:handler:)

**Framework**: GameKit  
**Kind**: method

Displays the Game Center dashboard in a state that shows a specific achievement.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func trigger(achievementID: String, handler: (() -> Void)? = nil)
```

## Parameters

- `achievementID`: The identifier for the achievement.
- `handler`: The block that GameKit calls after it displays the dashboard.

## See Also

- [var isFocused: Bool](gkaccesspoint/isfocused.md)
  A Boolean value that indicates whether the access point is in focus on tvOS.
- [func trigger(handler: () -> Void)](gkaccesspoint/trigger(handler:).md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(state: GKGameCenterViewControllerState, handler: () -> Void)](gkaccesspoint/trigger(state:handler:).md)
  Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.
- [func trigger(player: GKPlayer, handler: (() -> Void)?)](gkaccesspoint/trigger(player:handler:).md)
  Displays the Game Center dashboard in a state that shows a player profile.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardid:playerscope:timescope:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardsetid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(achievementid:handler:))*