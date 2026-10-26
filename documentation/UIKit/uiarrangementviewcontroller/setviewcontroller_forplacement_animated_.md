# setViewController:forPlacement:animated:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the view controller in the arrangement for a specific placement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
- (void) setViewController:(UIViewController *) viewController forPlacement:(UIArrangementViewControllerViewPlacement) placement animated:(BOOL) animated;
```

## Parameters

- `viewController`: The view controller in the arrangement.
- `placement`: The placement of the view controller in the arrangement.
- `animated`: Whether to animate the view controller transition.

## See Also

### Managing arrangement view controllers
- [UIArrangementViewControllerViewPlacement](../uiarrangementviewcontrollerviewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [- viewControllerForPlacement:](./viewcontrollerforplacement_.md)
  The view controller in the arrangement for the provided placement.
- [- setViewController:forPlacement:](./setviewcontroller_forplacement_.md)
  Sets the view controller in the arrangement for a specific placement.
- [- placementForViewController:](./placementforviewcontroller_.md)
  The placement for the provided view controller in the arrangement. Will return `UIArrangementViewControllerViewPlacementNone` if the provided view controller is not a view controller provided to the arrangement view controller with an explicit placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/setviewcontroller:forplacement:animated:)*