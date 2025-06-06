# makeView(element:existingView:)

**Framework**: TVMLKit  
**Kind**: method

Returns a view for a view element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func makeView(element: TVViewElement, existingView: UIView?) -> UIView?
```

## Mentions

- [Creating TVML Elements](creating-tvml-elements.md)

#### Return Value

The new view associated with the view element. If the app doesn’t handle the event, you must return `nil`.

#### Discussion

When possible, update the view contained in the `existingView` parameter instead of creating a new view. However, if the existing view is an instance of [`UICollectionViewCell`](https://developer.apple.com/documentation/UIKit/UICollectionViewCell), you must configure the cell instead of creating a new instance.

## Parameters

- `element`: The view element requesting a new view.
- `existingView`: The current view.

## See Also

- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:).md)
  Returns a view controller for a view element.
- [func collectionViewCellClass(for: TVViewElement) -> AnyClass?](tvinterfacecreating/collectionviewcellclass(for:).md)
  Returns a collection view cell for the specified element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](tvinterfacecreating/playerviewcontroller(for:).md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/makeview(element:existingview:))*