# playerViewController(for:)

**Framework**: TVMLKit  
**Kind**: method

Returns the custom player user interface for a custom player.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
optional func playerViewController(for player: TVPlayer) -> UIViewController?
```

#### Return Value

The new view controller associated with the view element. If the app doesn’t handle this event, you must return nil.

## Parameters

- `player`: The player requesting a view controller.

## See Also

- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:).md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](tvinterfacecreating/makeview(element:existingview:).md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](tvinterfacecreating/collectionviewcellclass(for:).md)
  Returns a collection view cell for the specified element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/playerviewcontroller(for:))*