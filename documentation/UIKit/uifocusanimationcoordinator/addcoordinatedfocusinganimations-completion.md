# addCoordinatedFocusingAnimations(_:completion:)

**Framework**: UIKit  
**Kind**: method

Runs the specified set of animations together with the system animations for adding focus to an item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addCoordinatedFocusingAnimations(_ animations: ((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)? = nil)
```

#### Discussion

When focus is being added to an item, use this method to coordinate your custom animations with the system animations. The animations you specify are run in the same animation block as the system animations. Use the information in the context parameter to determine any custom behaviors for your animations. For example, you might configure your animations to run in half the time as the main animation and start after a short delay.

## Parameters

- `animations`: A block object containing your focus-related animations. This block has no return value and takes the following parameter:
- `completion`: The block object to execute after the main animations completes. The specified animations are run in the same animation context as the main animation.

## See Also

- [func addCoordinatedUnfocusingAnimations(((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedunfocusinganimations(_:completion:).md)
  Runs the specified set of animations together with the system animations for removing focus from an item.
- [func addCoordinatedAnimations((() -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedanimations(_:completion:).md)
  Specifies the animations to coordinate with the active focus animation.
- [protocol UIFocusAnimationContext](uifocusanimationcontext.md)
  Information about focusing animations being performed by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/addcoordinatedfocusinganimations(_:completion:))*