# navigationControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method

Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationControllerPreferredInterfaceOrientationForPresentation(_ navigationController: UINavigationController) -> UIInterfaceOrientation
```

#### Return Value

The preferred orientation for presenting the navigation controller.

## Parameters

- `navigationController`: The navigation controller

## See Also

- [func navigationController(UINavigationController, animationControllerFor: UINavigationController.Operation, from: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:).md)
  Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [func navigationController(UINavigationController, interactionControllerFor: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:).md)
  Allows the delegate to return an interactive animator object for use during view controller transitions.
- [func navigationControllerSupportedInterfaceOrientations(UINavigationController) -> UIInterfaceOrientationMask](uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:))*