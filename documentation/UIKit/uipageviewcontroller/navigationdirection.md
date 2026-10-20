# UIPageViewController.NavigationDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Directions for page-turn transitions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum NavigationDirection
```

```c
enum UIPageViewControllerNavigationDirection : NSInteger;
```

#### Overview

For horizontal navigation, pages turn from the right side of the screen to the left as you navigate forward.

For vertical navigation, pages turn from the bottom of the screen to the top as you navigate forward.

## Topics

### Constants
- [UIPageViewController.NavigationDirection.forward](./navigationdirection/forward.md)
  Navigation to the next page.
- [UIPageViewController.NavigationDirection.reverse](./navigationdirection/reverse.md)
  Navigation to the previous page.
### Initializers
- [init?(rawValue: Int)](./navigationdirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing Content
- [func setViewControllers([UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](./setviewcontrollers%28_,direction,animated,completion%29.md)
  Sets the view controllers to be displayed.
- [var viewControllers: [UIViewController]?](./viewcontrollers.md)
  The view controllers displayed by the page view controller.
- [var gestureRecognizers: [UIGestureRecognizer]](./gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](../uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationdirection)*