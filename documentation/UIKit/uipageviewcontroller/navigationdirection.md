# UIPageViewController.NavigationDirection

**Framework**: UIKit  
**Kind**: enum

Directions for page-turn transitions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum NavigationDirection
```

#### Overview

For horizontal navigation, pages turn from the right side of the screen to the left as you navigate forward.

For vertical navigation, pages turn from the bottom of the screen to the top as you navigate forward.

## Topics

### Constants
- [UIPageViewController.NavigationDirection.forward](uipageviewcontroller/navigationdirection/forward.md)
  Navigation to the next page.
- [UIPageViewController.NavigationDirection.reverse](uipageviewcontroller/navigationdirection/reverse.md)
  Navigation to the previous page.
### Initializers
- [init?(rawValue: Int)](uipageviewcontroller/navigationdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:).md)
  Sets the view controllers to be displayed.
- [var viewControllers: [UIViewController]?](uipageviewcontroller/viewcontrollers.md)
  The view controllers displayed by the page view controller.
- [var gestureRecognizers: [UIGestureRecognizer]](uipageviewcontroller/gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationdirection)*