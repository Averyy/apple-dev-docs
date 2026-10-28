# leaderboardViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the leaderboard view is dismissed.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func leaderboardViewControllerDidFinish(_ viewController: GKLeaderboardViewController!)
```

```objc
- (void) leaderboardViewControllerDidFinish:(GKLeaderboardViewController *) viewController;
```

## Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The leaderboard view controller that was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontrollerdelegate/leaderboardviewcontrollerdidfinish(_:))*