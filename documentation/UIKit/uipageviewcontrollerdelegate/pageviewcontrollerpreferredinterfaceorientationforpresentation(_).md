# pageViewControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pageViewControllerPreferredInterfaceOrientationForPresentation(_ pageViewController: UIPageViewController) -> UIInterfaceOrientation
```

```objc
- (UIInterfaceOrientation) pageViewControllerPreferredInterfaceOrientationForPresentation:(UIPageViewController *) pageViewController;
```

## Return Value

The preferred orientation for presenting the page view controller.

## Parameters

- `pageViewController`: The page view controller.

## See Also

### Related Documentation
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
### Overriding View Rotation Settings
- [func pageViewControllerSupportedInterfaceOrientations(UIPageViewController) -> UIInterfaceOrientationMask](./pageviewcontrollersupportedinterfaceorientations%28_%29.md)
  Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:))*