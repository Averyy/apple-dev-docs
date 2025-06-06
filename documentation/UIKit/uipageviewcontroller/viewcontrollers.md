# viewControllers

**Framework**: UIKit  
**Kind**: property

The view controllers displayed by the page view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewControllers: [UIViewController]? { get }
```

## See Also

- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:).md)
  Sets the view controllers to be displayed.
- [UIPageViewController.NavigationDirection](uipageviewcontroller/navigationdirection.md)
  Directions for page-turn transitions.
- [var gestureRecognizers: [UIGestureRecognizer]](uipageviewcontroller/gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/viewcontrollers)*