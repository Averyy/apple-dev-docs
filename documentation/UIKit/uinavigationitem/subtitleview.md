# subtitleView

**Framework**: UIKit  
**Kind**: property

A custom view to display below the title in the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@NSCopying
@MainActor var subtitleView: UIView? { get set }
```

#### Discussion

If non-nil, this property takes precedence over the `subtitle` and `attributedSubtitle` properties. The view’s layout constraints will determine its size, or the view may override `sizeThatFits(_:)` to return its desired size.

## See Also

- [var centerItemGroups: [UIBarButtonItemGroup]](uinavigationitem/centeritemgroups.md)
  Customizable item groups to display in the center section of the navigation bar.
- [var leadingItemGroups: [UIBarButtonItemGroup]](uinavigationitem/leadingitemgroups.md)
  Item groups to display in the leading section of the navigation bar.
- [var trailingItemGroups: [UIBarButtonItemGroup]](uinavigationitem/trailingitemgroups.md)
  Item groups to display in the trailing section of the navigation bar.
- [var pinnedTrailingGroup: UIBarButtonItemGroup?](uinavigationitem/pinnedtrailinggroup.md)
  The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [var titleView: UIView?](uinavigationitem/titleview.md)
  A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [var largeSubtitleView: UIView?](uinavigationitem/largesubtitleview.md)
  A custom view to display below the large title.
- [var leftBarButtonItems: [UIBarButtonItem]?](uinavigationitem/leftbarbuttonitems.md)
  An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [var leftBarButtonItem: UIBarButtonItem?](uinavigationitem/leftbarbuttonitem.md)
  A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItems: [UIBarButtonItem]?](uinavigationitem/rightbarbuttonitems.md)
  An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItem: UIBarButtonItem?](uinavigationitem/rightbarbuttonitem.md)
  A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [func setLeftBarButtonItems([UIBarButtonItem]?, animated: Bool)](uinavigationitem/setleftbarbuttonitems(_:animated:).md)
  Sets the left bar button items, optionally animating the transition to the new items.
- [func setLeftBarButton(UIBarButtonItem?, animated: Bool)](uinavigationitem/setleftbarbutton(_:animated:).md)
  Sets the custom bar button item, optionally animating the transition to the new item.
- [func setRightBarButtonItems([UIBarButtonItem]?, animated: Bool)](uinavigationitem/setrightbarbuttonitems(_:animated:).md)
  Sets the right bar button items, optionally animating the transition to the new items.
- [func setRightBarButton(UIBarButtonItem?, animated: Bool)](uinavigationitem/setrightbarbutton(_:animated:).md)
  Sets the custom bar button item, optionally animating the transition to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/subtitleview)*