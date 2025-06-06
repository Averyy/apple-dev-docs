# backItem

**Framework**: UIKit  
**Kind**: property

The navigation item that is immediately below the topmost item on a navigation bar’s stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backItem: UINavigationItem? { get }
```

#### Discussion

If the [`leftBarButtonItem`](uinavigationitem/leftbarbuttonitem.md) property of the topmost navigation item is `nil`, the navigation bar displays a back button whose title is derived from the item in this property.

If there is only one item on the navigation bar’s stack, the value of this property is `nil`.

## See Also

- [func pushItem(UINavigationItem, animated: Bool)](uinavigationbar/pushitem(_:animated:).md)
  Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [func popItem(animated: Bool) -> UINavigationItem?](uinavigationbar/popitem(animated:).md)
  Pops the top item from the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](uinavigationbar/setitems(_:animated:).md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var items: [UINavigationItem]?](uinavigationbar/items.md)
  An array of navigation items managed by the navigation bar.
- [var topItem: UINavigationItem?](uinavigationbar/topitem.md)
  The navigation item at the top of the navigation bar’s stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backitem)*