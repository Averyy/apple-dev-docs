# achievementDelegate

**Framework**: GameKit  
**Kind**: property

The achievement view controller’s delegate.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var achievementDelegate: (any GKAchievementViewControllerDelegate)! { get set }
```

#### Discussion

Your game must set the delegate before presenting the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller/achievementdelegate)*