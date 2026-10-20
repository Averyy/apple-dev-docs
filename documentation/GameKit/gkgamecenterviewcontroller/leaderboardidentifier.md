# leaderboardIdentifier

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The named leaderboard that the view controller displays.

**Availability**:
- iOS 7.0+ - Deprecated in 14.0
- iPadOS 7.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(leaderboard:playerScope:)`](./init%28leaderboard,playerscope%29.md) instead.

## Declaration

```swift
var leaderboardIdentifier: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * leaderboardIdentifier;
```

#### Discussion

The [`leaderboardIdentifier`](./leaderboardidentifier.md) property must either be `nil` or it must match a leaderboard identifier you defined when you created your leaderboards in App Store Connect. If `nil`, the view displays scores for the aggregate leaderboard. Default is `nil`.

When the leaderboard is presented, the value of this property determines which leaderboard content is displayed to the player. As the player changes which leaderboard content they view, the [`leaderboardIdentifier`](./leaderboardidentifier.md) property is automatically updated. For example, to preserve the player’s selections, you can read the [`leaderboardIdentifier`](./leaderboardidentifier.md) property after the screen is dismissed, and set that value the next time you initialize the view controller.

## See Also

### Deprecated Properties
- [var viewState: GKGameCenterViewControllerState](./viewstate.md)
  The content that the Game Center controller displays.
- [var leaderboardCategory: String?](./leaderboardcategory.md)
  The named leaderboard that the view controller displays.
- [var leaderboardTimeScope: GKLeaderboard.TimeScope](./leaderboardtimescope.md)
  A time filter that restricts the scores to display to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/leaderboardidentifier)*