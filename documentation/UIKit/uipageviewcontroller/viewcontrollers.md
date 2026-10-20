# viewControllers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controllers displayed by the page view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var viewControllers: [UIViewController]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<__kindof UIViewController *> * viewControllers;
```

## See Also

### Providing Content
- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](./setviewcontrollers%28_,direction,animated,completion%29.md)
  Sets the view controllers to be displayed.
- [UIPageViewController.NavigationDirection](./navigationdirection.md)
  Directions for page-turn transitions.
- [var gestureRecognizers: [UIGestureRecognizer]](./gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](../uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/viewcontrollers)*