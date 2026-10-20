# setViewController(_:for:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the view controller in the arrangement for the specific placement you provide.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

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

### Managing arrangement view controllers
- [UIArrangementViewController.ViewPlacement](./viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](./viewcontroller%28for%29.md)
  Returns the view controller in the arrangement for the placement you provide.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](./placement%28for%29.md)
  Returns the placement for the view controller you provide in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/setviewcontroller(_:for:animated:))*