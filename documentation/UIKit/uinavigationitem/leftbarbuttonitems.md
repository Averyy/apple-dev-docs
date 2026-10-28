# leftBarButtonItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var leftBarButtonItems: [UIBarButtonItem]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<UIBarButtonItem *> * leftBarButtonItems;
```

## Discussion

This array can contain 0 or more bar items to display on the left (or leading) side of the navigation bar. Items can include fixed-width and flexible-width spaces. If the [`leftItemsSupplementBackButton`](./leftitemssupplementbackbutton.md) property is [`true`](../../Swift/true.md), the items are displayed to the right (or trailing side) of the Back button, otherwise the items replace the Back button and start at the left (or leading) edge of the bar. Items are displayed left-to-right in the same order as they appear in the array. In a right-to-left user interface, the items are automatically flipped.

If there is not enough room to display all of the items in the array, those that would overlap the title view (if present) or the buttons on the right side of the bar are not displayed.

The first item in the array can also be set using the [`leftBarButtonItem`](./leftbarbuttonitem.md) property.

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
- [func setRightBarButton(UIBarButtonItem?, animated: Bool)](./setrightbarbutton%28_,animated%29.md)
  Sets the custom bar button item, optionally animating the transition to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/leftbarbuttonitems)*