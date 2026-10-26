# placementForViewController:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

The placement for the provided view controller in the arrangement. Will return `UIArrangementViewControllerViewPlacementNone` if the provided view controller is not a view controller provided to the arrangement view controller with an explicit placement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
- (UIArrangementViewControllerViewPlacement) placementForViewController:(UIViewController *) viewController;
```

## Parameters

- `viewController`: The view controller in the arrangement.

## See Also

### Managing arrangement view controllers
- [UIArrangementViewControllerViewPlacement](../uiarrangementviewcontrollerviewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [- viewControllerForPlacement:](./viewcontrollerforplacement_.md)
  The view controller in the arrangement for the provided placement.
- [- setViewController:forPlacement:](./setviewcontroller_forplacement_.md)
  Sets the view controller in the arrangement for a specific placement.
- [- setViewController:forPlacement:animated:](./setviewcontroller_forplacement_animated_.md)
  Sets the view controller in the arrangement for a specific placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/placementforviewcontroller:)*