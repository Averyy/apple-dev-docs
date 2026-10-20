# leaderboardDelegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s delegate.

**Availability**:
- macOS
- visionOS

## Declaration

```swift
weak var leaderboardDelegate: (any GKLeaderboardViewControllerDelegate)! { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, weak) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate;
```

*macOS*

```objc
@property (atomic, weak) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate;
```

#### Discussion

Before displaying the leaderboard, you must set a delegate.

## See Also

### Configuring the Leaderboard View Controller
- [var category: String!](./category.md)
  The named leaderboard that is displayed by the view controller.
- [var timeScope: GKLeaderboard.TimeScope](./timescope.md)
  A time filter used to restrict which scores are displayed to the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/leaderboarddelegate)*