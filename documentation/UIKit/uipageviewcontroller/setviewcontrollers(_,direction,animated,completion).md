# setViewControllers(_:direction:animated:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the view controllers to be displayed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setViewControllers(_ viewControllers: [UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

```objc
- (void) setViewControllers:(NSArray<UIViewController *> *) viewControllers direction:(UIPageViewControllerNavigationDirection) direction animated:(BOOL) animated completion:(void (^)(BOOL finished)) completion;
```

## Discussion

The view controllers passed to this method are those that will be visible after the animation has completed. Use a data source to provide additional view controllers to which users navigate.

If the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](./transitionstyle-swift.enum/pagecurl.md), the view controllers to pass in the `viewControllers` parameter depends on the spine location and the value of the [`isDoubleSided`](./isdoublesided.md) property:

| Spine location | Double sided | What to pass |
| --- | --- | --- |
| [`UIPageViewController.SpineLocation.mid`](./spinelocation-swift.enum/mid.md) | [`true`](../../Swift/true.md) | Pass the page to be displayed on the left and the page to be displayed on the right. |
| [`UIPageViewController.SpineLocation.min`](./spinelocation-swift.enum/min.md) or [`UIPageViewController.SpineLocation.max`](./spinelocation-swift.enum/max.md) | [`true`](../../Swift/true.md) | Pass the front of the page to be displayed and the back of the previously-displayed page. The back is used for the page turning animation. |
| [`UIPageViewController.SpineLocation.min`](./spinelocation-swift.enum/min.md) or [`UIPageViewController.SpineLocation.max`](./spinelocation-swift.enum/max.md) | [`false`](../../Swift/false.md) | Pass the front of the page to be displayed. |

## Parameters

- `viewControllers`: The view controller or view controllers to be displayed.
- `direction`: The navigation direction.
- `animated`: A Boolean value that indicates whether the transition is to be animated.
- `completion`: A block to be called when the page-turn animation completes.

  The block takes the following parameters:

  - ***finished***: [`true`](../../Swift/true.md) if the animation finished; [`false`](../../Swift/false.md) if it was skipped.

## See Also

### Providing Content
- [UIPageViewController.NavigationDirection](./navigationdirection.md)
  Directions for page-turn transitions.
- [var viewControllers: [UIViewController]?](./viewcontrollers.md)
  The view controllers displayed by the page view controller.
- [var gestureRecognizers: [UIGestureRecognizer]](./gesturerecognizers.md)
  An array of [`UIGestureRecognizer`](../uigesturerecognizer.md) objects that are configured to handle user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:))*