# timeScope

**Framework**: GameKit  
**Kind**: property

A time filter used to restrict which scores are displayed to the player.

**Availability**:
- macOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var timeScope: GKLeaderboard.TimeScope { get set }
```

#### Discussion

This property determines which tab view is displayed to the player. The default value is [`GKLeaderboard.TimeScope.allTime`](gkleaderboard/timescope-swift.enum/alltime.md), which shows the best score each player has earned. For more information on time scopes, see [`GKLeaderboard`](gkleaderboard.md).

If the player changes which tab they view, the `timeScope` property is automatically updated. For example, you can read the `timeScope` property after the view controller is dismissed, and set that value the next time you initialize a new leaderboard view controller.

## See Also

- [var category: String!](gkleaderboardviewcontroller/category.md)
  The named leaderboard that is displayed by the view controller.
- [var leaderboardDelegate: (any GKLeaderboardViewControllerDelegate)!](gkleaderboardviewcontroller/leaderboarddelegate.md)
  The view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/timescope)*