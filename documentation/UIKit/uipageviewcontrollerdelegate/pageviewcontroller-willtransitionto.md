# pageViewController(_:willTransitionTo:)

**Framework**: UIKit  
**Kind**: method

Called before a gesture-driven transition begins.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionTo pendingViewControllers: [UIViewController])
```

#### Discussion

If the user aborts the navigation gesture, the transition doesn’t complete and the view controllers stay the same.

## Parameters

- `pageViewController`: The page view controller.
- `pendingViewControllers`: The view controllers that are being transitioned to.

## See Also

- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:).md)
  Called after a gesture-driven transition completes.
- [func pageViewController(UIPageViewController, spineLocationFor: UIInterfaceOrientation) -> UIPageViewController.SpineLocation](uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:).md)
  Returns the spine location for the given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:))*