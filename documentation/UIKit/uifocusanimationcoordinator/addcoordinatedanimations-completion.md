# addCoordinatedAnimations(_:completion:)

**Framework**: UIKit  
**Kind**: method

Specifies the animations to coordinate with the active focus animation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addCoordinatedAnimations(_ animations: (() -> Void)?, completion: (() -> Void)? = nil)
```

#### Discussion

Use this method to coordinate your custom animations with the system animations for adding or removing focus.

Unless the duration time is inherited, the specified animations may not run in the same context as the main animation. It is perfectly legitimate to specify only a completion block.

## Parameters

- `animations`: The animation to be run.
- `completion`: A block object to be executed after the main animation completes. Any animations specified are run in the same animation context as the main animation.

## See Also

- [func addCoordinatedFocusingAnimations(((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedfocusinganimations(_:completion:).md)
  Runs the specified set of animations together with the system animations for adding focus to an item.
- [func addCoordinatedUnfocusingAnimations(((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedunfocusinganimations(_:completion:).md)
  Runs the specified set of animations together with the system animations for removing focus from an item.
- [protocol UIFocusAnimationContext](uifocusanimationcontext.md)
  Information about focusing animations being performed by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/addcoordinatedanimations(_:completion:))*