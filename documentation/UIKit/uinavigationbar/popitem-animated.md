# popItem(animated:)

**Framework**: UIKit  
**Kind**: method

Pops the top item from the navigation bar’s stack and updates the UI.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func popItem(animated: Bool) -> UINavigationItem?
```

#### Return Value

The top item that was popped.

#### Discussion

Popping a navigation item removes the top item from the stack and replaces it with the back item. The back item’s title is centered on the navigation bar and its other properties are displayed.

## Parameters

- `animated`:   if the navigation bar should be animated; otherwise,  .

## See Also

- [func pushItem(UINavigationItem, animated: Bool)](uinavigationbar/pushitem(_:animated:).md)
  Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](uinavigationbar/setitems(_:animated:).md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var items: [UINavigationItem]?](uinavigationbar/items.md)
  An array of navigation items managed by the navigation bar.
- [var topItem: UINavigationItem?](uinavigationbar/topitem.md)
  The navigation item at the top of the navigation bar’s stack.
- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/popitem(animated:))*