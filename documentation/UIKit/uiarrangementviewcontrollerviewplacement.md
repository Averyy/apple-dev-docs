# UIArrangementViewControllerViewPlacement

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A placement of a view controller within an arrangement view controller.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```c
enum UIArrangementViewControllerViewPlacement : NSInteger;
```

#### Overview

You use a view placement to specify which position a view takes in an arrangement.

For more information on how an overlay arrangement presents primary and secondary views, see [`UIOverlayArrangement`](./uioverlayarrangement-c.class.md).

For more information on how a split arrangement presents primary and secondary views, see [`UISplitArrangement`](./uisplitarrangement-c.class.md).

## Topics

### Specifying a view placement
- [UIArrangementViewControllerViewPlacementNone](./uiarrangementviewcontrollerviewplacement/uiarrangementviewcontrollerviewplacementnone.md)
  A value that indicates the view controller has no placement in the arrangement.
- [UIArrangementViewControllerViewPlacementPrimary](./uiarrangementviewcontrollerviewplacement/uiarrangementviewcontrollerviewplacementprimary.md)
  The primary placement in the arrangement.
- [UIArrangementViewControllerViewPlacementSecondary](./uiarrangementviewcontrollerviewplacement/uiarrangementviewcontrollerviewplacementsecondary.md)
  The secondary placement in the arrangement.

## See Also

### Managing arrangement view controllers
- [- viewControllerForPlacement:](./uiarrangementviewcontroller/viewcontrollerforplacement_.md)
  The view controller in the arrangement for the provided placement.
- [- setViewController:forPlacement:](./uiarrangementviewcontroller/setviewcontroller_forplacement_.md)
  Sets the view controller in the arrangement for a specific placement.
- [- setViewController:forPlacement:animated:](./uiarrangementviewcontroller/setviewcontroller_forplacement_animated_.md)
  Sets the view controller in the arrangement for a specific placement.
- [- placementForViewController:](./uiarrangementviewcontroller/placementforviewcontroller_.md)
  The placement for the provided view controller in the arrangement. Will return `UIArrangementViewControllerViewPlacementNone` if the provided view controller is not a view controller provided to the arrangement view controller with an explicit placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontrollerviewplacement)*