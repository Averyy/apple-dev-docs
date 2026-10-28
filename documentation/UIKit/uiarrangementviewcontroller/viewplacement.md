# UIArrangementViewController.ViewPlacement

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A placement of a view controller within an arrangement view controller.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct ViewPlacement
```

## Overview

You use a view placement to specify which position a view takes in an arrangement.

For more information on how an overlay arrangement presents primary and secondary views, see [`UIOverlayArrangement`](../uioverlayarrangement-swift.struct.md).

For more information on how a split arrangement presents primary and secondary views, see [`UISplitArrangement`](../uisplitarrangement-swift.struct.md).

## Topics

### Getting a placement
- [static var primary: UIArrangementViewController.ViewPlacement](./viewplacement/primary.md)
  The primary placement in the arrangement.
- [static var secondary: UIArrangementViewController.ViewPlacement](./viewplacement/secondary.md)
  The secondary placement in the arrangement.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing arrangement view controllers
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](./viewcontroller%28for%29.md)
  Returns the view controller in the arrangement for the placement you provide.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](./setviewcontroller%28_,for,animated%29.md)
  Sets the view controller in the arrangement for the specific placement you provide.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](./placement%28for%29.md)
  Returns the placement for the view controller you provide in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewplacement)*