# placement(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the placement for the view controller you provide in the arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
@preconcurrency final func placement(for viewController: UIViewController) -> UIArrangementViewController.ViewPlacement?
```

## Discussion

Returns `nil` if the provided view controller isn’t one of the view controllers in the arrangement with a specific placement.

## Parameters

- `viewController`: The view controller to find in the arrangement.

## See Also

### Managing arrangement view controllers
- [UIArrangementViewController.ViewPlacement](./viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](./viewcontroller%28for%29.md)
  Returns the view controller in the arrangement for the placement you provide.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](./setviewcontroller%28_,for,animated%29.md)
  Sets the view controller in the arrangement for the specific placement you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/placement(for:))*