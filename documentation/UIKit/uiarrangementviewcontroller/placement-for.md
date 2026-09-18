# placement(for:)

**Framework**: UIKit  
**Kind**: method

Returns the placement for the provided view controller in the arrangement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency final func placement(for viewController: UIViewController) -> UIArrangementViewController.ViewPlacement?
```

#### Discussion

Returns `nil` if the provided view controller isn’t one of the view controllers in the arrangement with a specific placement.

## Parameters

- `viewController`: The view controller in the arrangement.

## See Also

- [UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](uiarrangementviewcontroller/viewcontroller(for:).md)
  The view controller in the arrangement for the provided placement.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](uiarrangementviewcontroller/setviewcontroller(_:for:animated:).md)
  Sets the view controller in the arrangement for a specific placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/placement(for:))*