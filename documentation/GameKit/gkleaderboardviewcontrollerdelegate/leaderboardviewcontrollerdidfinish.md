# leaderboardViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Called when the leaderboard view is dismissed.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func leaderboardViewControllerDidFinish(_ viewController: GKLeaderboardViewController!)
```

#### Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The leaderboard view controller that was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontrollerdelegate/leaderboardviewcontrollerdidfinish(_:))*