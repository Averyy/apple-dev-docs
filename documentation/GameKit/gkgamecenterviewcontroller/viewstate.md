# viewState

**Framework**: GameKit  
**Kind**: property

The content that the Game Center controller displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewState: GKGameCenterViewControllerState { get set }
```

#### Discussion

See [`GKGameCenterViewControllerState`](gkgamecenterviewcontrollerstate.md) for possible values. When you first present the Game Center view controller, the content displayed by the view controller is determined by this property. If the player navigates to different content, the view state is automatically updated. For example, to preserve the player’s selections, you can read the [`viewState`](gkgamecenterviewcontroller/viewstate.md) property after the screen is dismissed, and set that value the next time you initialize the view controller.

## See Also

- [var leaderboardIdentifier: String?](gkgamecenterviewcontroller/leaderboardidentifier.md)
  The named leaderboard that the view controller displays.
- [var leaderboardCategory: String?](gkgamecenterviewcontroller/leaderboardcategory.md)
  The named leaderboard that the view controller displays.
- [var leaderboardTimeScope: GKLeaderboard.TimeScope](gkgamecenterviewcontroller/leaderboardtimescope.md)
  A time filter that restricts the scores to display to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/viewstate)*