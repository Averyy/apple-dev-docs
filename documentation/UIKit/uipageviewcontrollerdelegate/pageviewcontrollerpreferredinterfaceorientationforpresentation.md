# pageViewControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method

Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pageViewControllerPreferredInterfaceOrientationForPresentation(_ pageViewController: UIPageViewController) -> UIInterfaceOrientation
```

#### Return Value

The preferred orientation for presenting the page view controller.

## Parameters

- `pageViewController`: The page view controller.

## See Also

- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func pageViewControllerSupportedInterfaceOrientations(UIPageViewController) -> UIInterfaceOrientationMask](uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:))*