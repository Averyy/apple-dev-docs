# pageViewController(_:didFinishAnimating:previousViewControllers:transitionCompleted:)

**Framework**: UIKit  
**Kind**: method

Called after a gesture-driven transition completes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers: [UIViewController], transitionCompleted completed: Bool)
```

#### Discussion

Use the `completed` parameter to distinguish between a transition that completed (the page was turned) and a transition that the user aborted (the page was not turned).

The value of the `previousViewControllers` parameter is the same as what the [`viewControllers`](uipageviewcontroller/viewcontrollers.md) method would have returned prior to the page turn.

## Parameters

- `pageViewController`: The page view controller.
- `finished`:   if the animation finished; otherwise,  .
- `previousViewControllers`: The view controllers prior to the transition.
- `completed`:   if the user completed the page-turn gesture; otherwise,  .

## See Also

- [func pageViewController(UIPageViewController, willTransitionTo: [UIViewController])](uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:).md)
  Called before a gesture-driven transition begins.
- [func pageViewController(UIPageViewController, spineLocationFor: UIInterfaceOrientation) -> UIPageViewController.SpineLocation](uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:).md)
  Returns the spine location for the given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:))*