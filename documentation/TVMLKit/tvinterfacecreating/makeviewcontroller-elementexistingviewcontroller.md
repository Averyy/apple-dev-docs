# makeViewController(element:existingViewController:)

**Framework**: TVMLKit  
**Kind**: method

Returns a view controller for a view element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?
```

#### Return Value

The new view controller associated with the view element. If the app doesn’t handle this event, you must return `nil`.

#### Discussion

When possible, update the view controller contained in the `existingViewController` parameter instead of creating a new view controller.

## Parameters

- `element`: The view element requesting a view controller.
- `existingViewController`: The current view controller.

## See Also

- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](tvinterfacecreating/makeview(element:existingview:).md)
  Returns a view for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](tvinterfacecreating/collectionviewcellclass(for:).md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](tvinterfacecreating/playerviewcontroller(for:).md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:))*