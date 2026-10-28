# collectionViewCellClass(for:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Returns a collection view cell for the specified element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func collectionViewCellClass(for element: TVViewElement) -> AnyClass?
```

```objc
- (Class) collectionViewCellClassForElement:(TVViewElement *) element;
```

## Return Value

The new collection view cell associated with the given element name.

## Discussion

The collection view cell must be in a list, shelf, or grid. This method is called once per unique element name as a common cell class is used for all elements that share the same name in a collection. Return `nil` for default handling.

## Parameters

- `element`: The element a collection view cell is created for.

## See Also

### Updating View Information
- [func makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](./makeviewcontroller%28element,existingviewcontroller%29.md)
  Returns a view controller for a view element.
- [func makeView(element: TVViewElement, existingView: UIView?) -> UIView?](./makeview%28element,existingview%29.md)
  Returns a view for a view element.
- [func playerViewController(for: TVPlayer) -> UIViewController?](./playerviewcontroller%28for%29.md)
  Returns the custom player user interface for a custom player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/collectionviewcellclass(for:))*