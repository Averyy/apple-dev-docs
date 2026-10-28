# isFocused

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the access point is in focus on tvOS.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
var isFocused: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isFocused) BOOL focused;
```

## Discussion

To change the focus to the access point, set this property to [`true`](../../Swift/true.md); otherwise, set it to [`false`](../../Swift/false.md).

## See Also

### Managing the access point
- [func trigger(handler: () -> Void)](./trigger%28handler%29.md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(state: GKGameCenterViewControllerState, handler: () -> Void)](./trigger%28state,handler%29.md)
  Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.
- [func trigger(player: GKPlayer, handler: (() -> Void)?)](./trigger%28player,handler%29.md)
  Displays the Game Center dashboard in a state that shows a player profile.
- [func trigger(achievementID: String, handler: (() -> Void)?)](./trigger%28achievementid,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific achievement.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](./trigger%28leaderboardid,playerscope,timescope,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](./trigger%28leaderboardsetid,handler%29.md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/isfocused)*