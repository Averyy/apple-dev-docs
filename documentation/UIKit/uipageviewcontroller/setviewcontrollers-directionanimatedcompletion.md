# setViewControllers(_:direction:animated:completion:)

**Framework**: UIKit  
**Kind**: method

Sets the view controllers to be displayed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setViewControllers(_ viewControllers: [UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

#### Discussion

The view controllers passed to this method are those that will be visible after the animation has completed. Use a data source to provide additional view controllers to which users navigate.

If the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md), the view controllers to pass in the `viewControllers` parameter depends on the spine location and the value of the [`isDoubleSided`](uipageviewcontroller/isdoublesided.md) property:

| Spine location | Double sided | What to pass |
| --- | --- | --- |
| [`UIPageViewController.SpineLocation.mid`](uipageviewcontroller/spinelocation-swift.enum/mid.md) | [`true`](https://developer.apple.com/documentation/swift/true) | Pass the page to be displayed on the left and the page to be displayed on the right. |
| [`UIPageViewController.SpineLocation.min`](uipageviewcontroller/spinelocation-swift.enum/min.md) or [`UIPageViewController.SpineLocation.max`](uipageviewcontroller/spinelocation-swift.enum/max.md) | [`true`](https://developer.apple.com/documentation/swift/true) | Pass the front of the page to be displayed and the back of the previously-displayed page. The back is used for the page turning animation. |
| [`UIPageViewController.SpineLocation.min`](uipageviewcontroller/spinelocation-swift.enum/min.md) or [`UIPageViewController.SpineLocation.max`](uipageviewcontroller/spinelocation-swift.enum/max.md) | [`false`](https://developer.apple.com/documentation/swift/false) | Pass the front of the page to be displayed. |

## Parameters

- `viewControllers`: The view controller or view controllers to be displayed.
- `direction`: The navigation direction.
- `animated`: A Boolean value that indicates whether the transition is to be animated.
- `completion`: The block takes the following parameters:

## See Also

- [UIPageViewController.NavigationDirection](uipageviewcontroller/navigationdirection.md)
  Directions for page-turn transitions.
- [var viewControllers: [UIViewController]?](uipageviewcontroller/viewcontrollers.md)
  The view controllers displayed by the page view controller.
- [var gestureRecognizers: [UIGestureRecognizer]](uipageviewcontroller/gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:))*