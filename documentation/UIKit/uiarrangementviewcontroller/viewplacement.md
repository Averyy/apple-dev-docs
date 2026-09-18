# UIArrangementViewController.ViewPlacement

**Framework**: UIKit  
**Kind**: struct

A placement of a view controller within an arrangement view controller.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct ViewPlacement
```

## Topics

### Getting a placement
- [static var primary: UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement/primary.md)
  The primary placement in the arrangement.
- [static var secondary: UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement/secondary.md)
  The secondary placement in the arrangement.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](uiarrangementviewcontroller/viewcontroller(for:).md)
  The view controller in the arrangement for the provided placement.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](uiarrangementviewcontroller/setviewcontroller(_:for:animated:).md)
  Sets the view controller in the arrangement for a specific placement.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](uiarrangementviewcontroller/placement(for:).md)
  Returns the placement for the provided view controller in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewplacement)*