# pageViewController(_:spineLocationFor:)

**Framework**: UIKit  
**Kind**: method

Returns the spine location for the given orientation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pageViewController(_ pageViewController: UIPageViewController, spineLocationFor orientation: UIInterfaceOrientation) -> UIPageViewController.SpineLocation
```

#### Return Value

The spine location.

#### Discussion

Use this method to change the spine location when the device orientation changes, as well as setting new view controllers and changing the double-sided state.

This method is called only if the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md).

## Parameters

- `pageViewController`: The page view controller
- `orientation`: The new orientation.

## See Also

- [func pageViewController(UIPageViewController, willTransitionTo: [UIViewController])](uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:).md)
  Called before a gesture-driven transition begins.
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:).md)
  Called after a gesture-driven transition completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:))*