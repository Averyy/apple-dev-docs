# pushItem(_:animated:)

**Framework**: UIKit  
**Kind**: method

Pushes the given navigation item onto the navigation bar’s stack and updates the UI.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pushItem(_ item: UINavigationItem, animated: Bool)
```

#### Discussion

Pushing a navigation item displays the item’s title in the center on the navigation bar. The previous top navigation item (if it exists) is displayed as a Back button on the left side of the navigation bar. If the new top item has a left custom view, it is displayed instead of the back button.

## Parameters

- `item`: The navigation item to push on the stack.
- `animated`:   if the navigation bar should be animated; otherwise,  .

## See Also

- [func popItem(animated: Bool) -> UINavigationItem?](uinavigationbar/popitem(animated:).md)
  Pops the top item from the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](uinavigationbar/setitems(_:animated:).md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var items: [UINavigationItem]?](uinavigationbar/items.md)
  An array of navigation items managed by the navigation bar.
- [var topItem: UINavigationItem?](uinavigationbar/topitem.md)
  The navigation item at the top of the navigation bar’s stack.
- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/pushitem(_:animated:))*