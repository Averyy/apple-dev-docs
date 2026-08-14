# isFocused

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the access point is in focus on tvOS.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
var isFocused: Bool { get set }
```

#### Discussion

To change the focus to the access point, set this property to [`true`](https://developer.apple.com/documentation/swift/true); otherwise, set it to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func trigger(handler: () -> Void)](gkaccesspoint/trigger(handler:).md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(state: GKGameCenterViewControllerState, handler: () -> Void)](gkaccesspoint/trigger(state:handler:).md)
  Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.
- [func trigger(player: GKPlayer, handler: (() -> Void)?)](gkaccesspoint/trigger(player:handler:).md)
  Displays the Game Center dashboard in a state that shows a player profile.
- [func trigger(achievementID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(achievementid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific achievement.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardid:playerscope:timescope:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardsetid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/isfocused)*