# titleView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A custom view that displays in the center of the navigation bar when the receiver is the top item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var titleView: UIView? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) UIView * titleView;
```

## Discussion

If this property value is `nil`, the navigation item’s title is displayed in the center of the navigation bar when the receiver is the top item. If you set this property to a custom title, it is displayed instead of the title.

Custom views can contain buttons. Use the [`init(type:)`](../uibutton/init%28type%29.md) method in [`UIButton`](../uibutton.md) class to add buttons to your custom view in the style of the navigation bar. Custom title views are centered on the navigation bar and may be resized to fit.

The default value is `nil`.

> **Note**:  `NSToolbar` doesn’t support a custom title view when the system displays the navigation bar’s content in a toolbar for an app built with Mac Catalyst. For more information, see [Display content in a toolbar on Mac](./title.md#Display-content-in-a-toolbar-on-Mac).

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
- [func setRightBarButton(UIBarButtonItem?, animated: Bool)](./setrightbarbutton%28_,animated%29.md)
  Sets the custom bar button item, optionally animating the transition to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titleview)*