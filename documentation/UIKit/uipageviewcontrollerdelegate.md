# UIPageViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The delegate of a page view controller must adopt the [`UIPageViewControllerDelegate`](uipageviewcontrollerdelegate.md) protocol. These methods allow the delegate to receive a notification when the device orientation changes and when the user navigates to a new page. For page-curl style transitions, the delegate can provide a different spine location in response to a change in the interface orientation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIPageViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to Page View Controller Events
- [func pageViewController(UIPageViewController, willTransitionTo: [UIViewController])](uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:).md)
  Called before a gesture-driven transition begins.
- [func pageViewController(UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:).md)
  Called after a gesture-driven transition completes.
- [func pageViewController(UIPageViewController, spineLocationFor: UIInterfaceOrientation) -> UIPageViewController.SpineLocation](uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:).md)
  Returns the spine location for the given orientation.
### Overriding View Rotation Settings
- [func pageViewControllerSupportedInterfaceOrientations(UIPageViewController) -> UIInterfaceOrientationMask](uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.
- [func pageViewControllerPreferredInterfaceOrientationForPresentation(UIPageViewController) -> UIInterfaceOrientation](uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIPageViewControllerDelegate)?](uipageviewcontroller/delegate.md)
  The delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate)*