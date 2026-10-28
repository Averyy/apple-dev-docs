# playerViewController(for:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Returns the custom player user interface for a custom player.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func playerViewController(for player: TVPlayer) -> UIViewController?
```

```objc
- (UIViewController *) playerViewControllerForPlayer:(TVPlayer *) player;
```

## Return Value

The new view controller associated with the view element. If the app doesn’t handle this event, you must return nil.

## Parameters

- `player`: The player requesting a view controller.

## See Also

### Updating View Information
- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](./makeviewcontroller%28element,existingviewcontroller%29.md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](./makeview%28element,existingview%29.md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](./collectionviewcellclass%28for%29.md)
  Returns a collection view cell for the specified element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/playerviewcontroller(for:))*