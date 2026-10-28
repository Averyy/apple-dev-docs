# achievementDelegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The achievement view controller’s delegate.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
weak var achievementDelegate: (any GKAchievementViewControllerDelegate)! { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, weak) id<GKAchievementViewControllerDelegate> achievementDelegate;
```

*macOS*

```objc
@property (atomic, weak) id<GKAchievementViewControllerDelegate> achievementDelegate;
```

## Discussion

Your game must set the delegate before presenting the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller/achievementdelegate)*