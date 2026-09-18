# setViewController(_:for:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the view controller in the arrangement for a specific placement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency final func setViewController(_ viewController: UIViewController?, for placement: UIArrangementViewController.ViewPlacement, animated: Bool = false)
```

## Parameters

- `viewController`: The view controller to place in the arrangement, or `nil` to remove the view controller currently in the placement.
- `placement`: The placement of the view controller in the arrangement.
- `animated`: Whether to animate the view controller transition.

## See Also

- [UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](uiarrangementviewcontroller/viewcontroller(for:).md)
  The view controller in the arrangement for the provided placement.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](uiarrangementviewcontroller/placement(for:).md)
  Returns the placement for the provided view controller in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/setviewcontroller(_:for:animated:))*