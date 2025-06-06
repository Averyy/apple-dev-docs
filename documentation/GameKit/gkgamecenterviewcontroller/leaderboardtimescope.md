# leaderboardTimeScope

**Framework**: GameKit  
**Kind**: property

A time filter that restricts the scores to display to the player.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var leaderboardTimeScope: GKLeaderboard.TimeScope { get set }
```

#### Discussion

This property determines which tab view of the scores screen is displayed to the player. The default value is [`GKLeaderboard.TimeScope.allTime`](gkleaderboard/timescope-swift.enum/alltime.md), which shows the best score each player has earned. For more information on time scopes, see [`GKLeaderboard`](gkleaderboard.md).

When the leaderboard is presented, the value of this property determines the initial tab that is displayed to the player. As the player changes which tab they view, the [`leaderboardTimeScope`](gkgamecenterviewcontroller/leaderboardtimescope.md) property is automatically updated. For example, to preserve the player’s selections, you can read the [`leaderboardTimeScope`](gkgamecenterviewcontroller/leaderboardtimescope.md) property after the screen is dismissed, and set that value the next time you initialize the view controller.

## See Also

- [var viewState: GKGameCenterViewControllerState](gkgamecenterviewcontroller/viewstate.md)
  The content that the Game Center controller displays.
- [var leaderboardIdentifier: String?](gkgamecenterviewcontroller/leaderboardidentifier.md)
  The named leaderboard that the view controller displays.
- [var leaderboardCategory: String?](gkgamecenterviewcontroller/leaderboardcategory.md)
  The named leaderboard that the view controller displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/leaderboardtimescope)*