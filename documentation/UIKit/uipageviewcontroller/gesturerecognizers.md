# gestureRecognizers

**Framework**: UIKit  
**Kind**: property

An array of [`UIGestureRecognizer`](uigesturerecognizer.md) objects that are configured to handle user interaction.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var gestureRecognizers: [UIGestureRecognizer] { get }
```

#### Discussion

These gesture recognizers are initially attached to a view in the page view controller’s hierarchy. To change the region of the screen in which the user can navigate using gestures,  they can be placed on another view.

## See Also

- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:).md)
  Sets the view controllers to be displayed.
- [UIPageViewController.NavigationDirection](uipageviewcontroller/navigationdirection.md)
  Directions for page-turn transitions.
- [var viewControllers: [UIViewController]?](uipageviewcontroller/viewcontrollers.md)
  The view controllers displayed by the page view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/gesturerecognizers)*