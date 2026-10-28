# makeViewController(element:existingViewController:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Returns a view controller for a view element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?
```

```objc
- (UIViewController *) viewControllerForElement:(TVViewElement *) element existingViewController:(UIViewController *) existingViewController;
```

## Return Value

The new view controller associated with the view element. If the app doesn’t handle this event, you must return `nil`.

## Discussion

When possible, update the view controller contained in the `existingViewController` parameter instead of creating a new view controller.

## Parameters

- `element`: The view element requesting a view controller.
- `existingViewController`: The current view controller.

## See Also

### Updating View Information
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](./makeview%28element,existingview%29.md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](./collectionviewcellclass%28for%29.md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](./playerviewcontroller%28for%29.md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:))*