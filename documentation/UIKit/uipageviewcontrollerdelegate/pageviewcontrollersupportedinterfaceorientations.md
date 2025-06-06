# pageViewControllerSupportedInterfaceOrientations(_:)

**Framework**: UIKit  
**Kind**: method

Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> UIInterfaceOrientationMask
```

#### Return Value

One of the [`UIInterfaceOrientationMask`](uiinterfaceorientationmask.md) constants that represents the set of   interface orientations supported by the page view controller.

## Parameters

- `pageViewController`: The page view controller.

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [func pageViewControllerPreferredInterfaceOrientationForPresentation(UIPageViewController) -> UIInterfaceOrientation](uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(_:))*