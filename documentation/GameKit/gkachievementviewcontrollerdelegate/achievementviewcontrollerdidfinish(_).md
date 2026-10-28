# achievementViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the user dismisses the achievements user interface.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func achievementViewControllerDidFinish(_ viewController: GKAchievementViewController!)
```

```objc
- (void) achievementViewControllerDidFinish:(GKAchievementViewController *) viewController;
```

## Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The achievement view controller whose interface was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontrollerdelegate/achievementviewcontrollerdidfinish(_:))*