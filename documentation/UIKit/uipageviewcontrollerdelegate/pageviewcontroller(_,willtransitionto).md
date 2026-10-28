# pageViewController(_:willTransitionTo:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called before a gesture-driven transition begins.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionTo pendingViewControllers: [UIViewController])
```

```objc
- (void) pageViewController:(UIPageViewController *) pageViewController willTransitionToViewControllers:(NSArray<UIViewController *> *) pendingViewControllers;
```

## Discussion

If the user aborts the navigation gesture, the transition doesn’t complete and the view controllers stay the same.

## Parameters

- `pageViewController`: The page view controller.
- `pendingViewControllers`: The view controllers that are being transitioned to.

## See Also

### Responding to Page View Controller Events
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](./pageviewcontroller%28_,didfinishanimating,previousviewcontrollers,transitioncompleted%29.md)
  Called after a gesture-driven transition completes.
- [func pageViewController(UIPageViewController, spineLocationFor: UIInterfaceOrientation) -> UIPageViewController.SpineLocation](./pageviewcontroller%28_,spinelocationfor%29.md)
  Returns the spine location for the given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:))*