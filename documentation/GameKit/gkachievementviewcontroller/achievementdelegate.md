# achievementDelegate

**Framework**: GameKit  
**Kind**: property

The achievement view controller’s delegate.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 4.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
weak var achievementDelegate: (any GKAchievementViewControllerDelegate)! { get set }
```

#### Discussion

Your game must set the delegate before presenting the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller/achievementdelegate)*