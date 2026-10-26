# attributedTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An attributed string that is rendered as the title in the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedTitle;
```

#### Discussion

If `titleView` is non-nil, this property is ignored.

An attributed string that the system renders as the title in the navigation bar.

#### Discussion

If [`titleView`](./titleview.md) is non-`nil`, the system ignores this property.

> **Note**:  `NSToolbar` doesn’t support an attributed title when the system displays the navigation bar’s content in a toolbar for an app built with Mac Catalyst. For more information, see [Display content in a toolbar on Mac](./title.md#Display-content-in-a-toolbar-on-Mac).

## See Also

### Configuring the title
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
- [var largeTitle: String?](./largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/attributedtitle-9l8p2)*