# leaderboardDelegate

**Framework**: GameKit  
**Kind**: property

The view controller’s delegate.

**Availability**:
- macOS ?+
- visionOS ?+

## Declaration

```swift
weak var leaderboardDelegate: (any GKLeaderboardViewControllerDelegate)! { get set }
```

#### Discussion

Before displaying the leaderboard, you must set a delegate.

## See Also

- [var category: String!](gkleaderboardviewcontroller/category.md)
  The named leaderboard that is displayed by the view controller.
- [var timeScope: GKLeaderboard.TimeScope](gkleaderboardviewcontroller/timescope.md)
  A time filter used to restrict which scores are displayed to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/leaderboarddelegate)*