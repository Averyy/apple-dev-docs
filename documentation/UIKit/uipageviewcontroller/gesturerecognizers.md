# gestureRecognizers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of [`UIGestureRecognizer`](../uigesturerecognizer.md) objects that are configured to handle user interaction.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var gestureRecognizers: [UIGestureRecognizer] { get }
```

```objc
@property (nonatomic, readonly) NSArray<__kindof UIGestureRecognizer *> * gestureRecognizers;
```

## Discussion

These gesture recognizers are initially attached to a view in the page view controller’s hierarchy. To change the region of the screen in which the user can navigate using gestures,  they can be placed on another view.

## See Also

### Providing Content
- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](./setviewcontrollers%28_,direction,animated,completion%29.md)
  Sets the view controllers to be displayed.
- [UIPageViewController.NavigationDirection](./navigationdirection.md)
  Directions for page-turn transitions.
- [var viewControllers: [UIViewController]?](./viewcontrollers.md)
  The view controllers displayed by the page view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/gesturerecognizers)*