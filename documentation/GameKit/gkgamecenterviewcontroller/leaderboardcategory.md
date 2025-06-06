# leaderboardCategory

**Framework**: GameKit  
**Kind**: property

The named leaderboard that the view controller displays.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var leaderboardCategory: String? { get set }
```

#### Discussion

The category property must either be `nil` or it must match a category identifier you defined when you created your leaderboards in App Store Connect. If `nil`, the view displays scores for the aggregate leaderboard. Default is `nil`.

When the leaderboard is presented, the value of this property determines which leaderboard content is displayed to the player. As the player changes which leaderboard content they view, the [`leaderboardCategory`](gkgamecenterviewcontroller/leaderboardcategory.md) property is automatically updated. For example, to preserve the player’s selections, you can read the [`leaderboardCategory`](gkgamecenterviewcontroller/leaderboardcategory.md) property after the screen is dismissed, and set that value the next time you initialize the view controller.

## See Also

- [var viewState: GKGameCenterViewControllerState](gkgamecenterviewcontroller/viewstate.md)
  The content that the Game Center controller displays.
- [var leaderboardIdentifier: String?](gkgamecenterviewcontroller/leaderboardidentifier.md)
  The named leaderboard that the view controller displays.
- [var leaderboardTimeScope: GKLeaderboard.TimeScope](gkgamecenterviewcontroller/leaderboardtimescope.md)
  A time filter that restricts the scores to display to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/leaderboardcategory)*