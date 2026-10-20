# setRightBarButton(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the custom bar button item, optionally animating the transition to the view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setRightBarButton(_ item: UIBarButtonItem?, animated: Bool)
```

```objc
- (void) setRightBarButtonItem:(UIBarButtonItem *) item animated:(BOOL) animated;
```

#### Discussion

If two navigation items have the same custom left or right bar button items, those bar button items remain stationary during the transition when the navigation item is pushed or popped.

## Parameters

- `item`: A custom bar item to display on the right of the navigation bar.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the transition to the custom bar item when this item is the top item. Specify [`false`](../../Swift/false.md) to set the item immediately without animating the change.

## See Also

### Specifying custom views
- [var centerItemGroups: [UIBarButtonItemGroup]](./centeritemgroups.md)
  Customizable item groups to display in the center section of the navigation bar.
- [var leadingItemGroups: [UIBarButtonItemGroup]](./leadingitemgroups.md)
  Item groups to display in the leading section of the navigation bar.
- [var trailingItemGroups: [UIBarButtonItemGroup]](./trailingitemgroups.md)
  Item groups to display in the trailing section of the navigation bar.
- [var pinnedTrailingGroup: UIBarButtonItemGroup?](./pinnedtrailinggroup.md)
  The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [var titleView: UIView?](./titleview.md)
  A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [var subtitleView: UIView?](./subtitleview.md)
  A custom view to display below the title in the navigation bar.
- [var largeSubtitleView: UIView?](./largesubtitleview.md)
  A custom view to display below the large title.
- [var leftBarButtonItems: [UIBarButtonItem]?](./leftbarbuttonitems.md)
  An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [var leftBarButtonItem: UIBarButtonItem?](./leftbarbuttonitem.md)
  A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItems: [UIBarButtonItem]?](./rightbarbuttonitems.md)
  An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItem: UIBarButtonItem?](./rightbarbuttonitem.md)
  A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [func setLeftBarButtonItems([UIBarButtonItem]?, animated: Bool)](./setleftbarbuttonitems%28_,animated%29.md)
  Sets the left bar button items, optionally animating the transition to the new items.
- [func setLeftBarButton(UIBarButtonItem?, animated: Bool)](./setleftbarbutton%28_,animated%29.md)
  Sets the custom bar button item, optionally animating the transition to the new item.
- [func setRightBarButtonItems([UIBarButtonItem]?, animated: Bool)](./setrightbarbuttonitems%28_,animated%29.md)
  Sets the right bar button items, optionally animating the transition to the new items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/setrightbarbutton(_:animated:))*