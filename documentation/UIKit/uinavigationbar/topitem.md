# topItem

**Framework**: UIKit  
**Kind**: property

The navigation item at the top of the navigation bar’s stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var topItem: UINavigationItem? { get }
```

## See Also

- [func pushItem(UINavigationItem, animated: Bool)](uinavigationbar/pushitem(_:animated:).md)
  Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [func popItem(animated: Bool) -> UINavigationItem?](uinavigationbar/popitem(animated:).md)
  Pops the top item from the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](uinavigationbar/setitems(_:animated:).md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var items: [UINavigationItem]?](uinavigationbar/items.md)
  An array of navigation items managed by the navigation bar.
- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/topitem)*