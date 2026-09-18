# viewController(for:)

**Framework**: UIKit  
**Kind**: method

The view controller in the arrangement for the provided placement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency final func viewController(for placement: UIArrangementViewController.ViewPlacement) -> UIViewController?
```

## Parameters

- `placement`: The placement of the view controller.

## See Also

- [UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](uiarrangementviewcontroller/setviewcontroller(_:for:animated:).md)
  Sets the view controller in the arrangement for a specific placement.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](uiarrangementviewcontroller/placement(for:).md)
  Returns the placement for the provided view controller in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewcontroller(for:))*