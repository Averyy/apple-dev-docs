# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of navigation items managed by the navigation bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var items: [UINavigationItem]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UINavigationItem *> * items;
```

## Discussion

The bottom item is at index `0`, the back item is at index `n-2`, and the top item is at index `n-1`, where `n` is the number of items in the array.

## See Also

### Pushing and popping items
- [func pushItem(UINavigationItem, animated: Bool)](./pushitem%28_,animated%29.md)
  Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [func popItem(animated: Bool) -> UINavigationItem?](./popitem%28animated%29.md)
  Pops the top item from the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](./setitems%28_,animated%29.md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var topItem: UINavigationItem?](./topitem.md)
  The navigation item at the top of the navigation bar’s stack.
- [var backItem: UINavigationItem?](./backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/items)*