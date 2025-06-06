# collectionViewCellClass(for:)

**Framework**: TVMLKit  
**Kind**: method

Returns a collection view cell for the specified element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func collectionViewCellClass(for element: TVViewElement) -> AnyClass?
```

#### Return Value

The new collection view cell associated with the given element name.

#### Discussion

The collection view cell must be in a list, shelf, or grid. This method is called once per unique element name as a common cell class is used for all elements that share the same name in a collection. Return `nil` for default handling.

## Parameters

- `element`: The element a collection view cell is created for.

## See Also

- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](tvinterfacecreating/makeviewcontroller(element:existingviewcontroller:).md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](tvinterfacecreating/makeview(element:existingview:).md)
  Returns a view for a view element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](tvinterfacecreating/playerviewcontroller(for:).md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/collectionviewcellclass(for:))*