# pageViewController(_:spineLocationFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the spine location for the given orientation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pageViewController(_ pageViewController: UIPageViewController, spineLocationFor orientation: UIInterfaceOrientation) -> UIPageViewController.SpineLocation
```

```objc
- (UIPageViewControllerSpineLocation) pageViewController:(UIPageViewController *) pageViewController spineLocationForInterfaceOrientation:(UIInterfaceOrientation) orientation;
```

#### Return Value

The spine location.

#### Discussion

Use this method to change the spine location when the device orientation changes, as well as setting new view controllers and changing the double-sided state.

This method is called only if the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](../uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md).

## Parameters

- `pageViewController`: The page view controller
- `orientation`: The new orientation.

## See Also

### Responding to Page View Controller Events
- [func pageViewController(UIPageViewController, willTransitionTo: [UIViewController])](./pageviewcontroller%28_,willtransitionto%29.md)
  Called before a gesture-driven transition begins.
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](./pageviewcontroller%28_,didfinishanimating,previousviewcontrollers,transitioncompleted%29.md)
  Called after a gesture-driven transition completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:))*