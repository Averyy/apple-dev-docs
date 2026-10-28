# trigger(handler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Displays the Game Center dashboard as if the player taps or presses the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func trigger(handler: @escaping () -> Void)
```

```objc
- (void) triggerAccessPointWithHandler:(void (^)()) handler;
```

## Discussion

For games that use controllers or the Apple TV remote, you can use this method to programmatically display the dashboard.

## Parameters

- `handler`: The block that GameKit calls after it displays the dashboard.

## See Also

### Managing the access point
- [var isFocused: Bool](./isfocused.md)
  A Boolean value that indicates whether the access point is in focus on tvOS.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(handler:))*