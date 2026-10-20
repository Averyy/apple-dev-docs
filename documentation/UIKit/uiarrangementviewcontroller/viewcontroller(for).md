# viewController(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the view controller in the arrangement for the placement you provide.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
@preconcurrency final func viewController(for placement: UIArrangementViewController.ViewPlacement) -> UIViewController?
```

## Parameters

- `placement`: The placement of the view controller.

## See Also

### Managing arrangement view controllers
- [UIArrangementViewController.ViewPlacement](./viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](./setviewcontroller%28_,for,animated%29.md)
  Sets the view controller in the arrangement for the specific placement you provide.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](./placement%28for%29.md)
  Returns the placement for the view controller you provide in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewcontroller(for:))*