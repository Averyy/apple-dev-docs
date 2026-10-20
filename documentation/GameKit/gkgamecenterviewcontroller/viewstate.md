# viewState

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The content that the Game Center controller displays.

**Availability**:
- iOS 6.0+ - Deprecated in 14.0
- iPadOS 6.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.9+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(state:)`](./init%28state%29.md) instead.

## Declaration

```swift
var viewState: GKGameCenterViewControllerState { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) GKGameCenterViewControllerState viewState;
```

*macOS*

```objc
@property (atomic, assign) GKGameCenterViewControllerState viewState;
```

#### Discussion

See [`GKGameCenterViewControllerState`](../gkgamecenterviewcontrollerstate.md) for possible values. When you first present the Game Center view controller, the content displayed by the view controller is determined by this property. If the player navigates to different content, the view state is automatically updated. For example, to preserve the player’s selections, you can read the [`viewState`](./viewstate.md) property after the screen is dismissed, and set that value the next time you initialize the view controller.

## See Also

### Deprecated Properties
- [var leaderboardIdentifier: String?](./leaderboardidentifier.md)
  The named leaderboard that the view controller displays.
- [var leaderboardCategory: String?](./leaderboardcategory.md)
  The named leaderboard that the view controller displays.
- [var leaderboardTimeScope: GKLeaderboard.TimeScope](./leaderboardtimescope.md)
  A time filter that restricts the scores to display to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/viewstate)*