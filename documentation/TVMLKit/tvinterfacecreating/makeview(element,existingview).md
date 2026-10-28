# makeView(element:existingView:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Returns a view for a view element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func makeView(element: TVViewElement, existingView: UIView?) -> UIView?
```

```objc
- (UIView *) viewForElement:(TVViewElement *) element existingView:(UIView *) existingView;
```

## Mentions

- [Creating TVML Elements](../creating-tvml-elements.md)

## Return Value

The new view associated with the view element. If the app doesn’t handle the event, you must return `nil`.

## Discussion

When possible, update the view contained in the `existingView` parameter instead of creating a new view. However, if the existing view is an instance of [`UICollectionViewCell`](../../UIKit/uicollectionviewcell.md), you must configure the cell instead of creating a new instance.

## Parameters

- `element`: The view element requesting a new view.
- `existingView`: The current view.

## See Also

### Updating View Information
- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](./makeviewcontroller%28element,existingviewcontroller%29.md)
  Returns a view controller for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](./collectionviewcellclass%28for%29.md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](./playerviewcontroller%28for%29.md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/makeview(element:existingview:))*