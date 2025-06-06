# trigger(state:handler:)

**Framework**: GameKit  
**Kind**: method

Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func trigger(state: GKGameCenterViewControllerState, handler: @escaping () -> Void)
```

## Mentions

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)

#### Discussion

For games that use controllers or the Apple TV remote, you can use this method to programmatically display the dashboard.

## Parameters

- `state`: The type of content to present.
- `handler`: The block that GameKit calls after it displays the dashboard.

## See Also

- [var isFocused: Bool](gkaccesspoint/isfocused.md)
  A Boolean value that indicates whether the access point is in focus on tvOS.
- [func trigger(handler: () -> Void)](gkaccesspoint/trigger(handler:).md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(player: GKPlayer, handler: (() -> Void)?)](gkaccesspoint/trigger(player:handler:).md)
  Displays the Game Center dashboard in a state that shows a player profile.
- [func trigger(achievementID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(achievementid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific achievement.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardid:playerscope:timescope:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardsetid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(state:handler:))*