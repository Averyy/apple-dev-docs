# achievementViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Called when the user dismisses the achievements user interface.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func achievementViewControllerDidFinish(_ viewController: GKAchievementViewController!)
```

#### Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The achievement view controller whose interface was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontrollerdelegate/achievementviewcontrollerdidfinish(_:))*