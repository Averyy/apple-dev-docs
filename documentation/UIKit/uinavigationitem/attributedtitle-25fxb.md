# attributedTitle

**Framework**: UIKit  
**Kind**: property

An attributed string that the system renders as the title in the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var attributedTitle: AttributedString? { get set }
```

#### Discussion

If [`titleView`](uinavigationitem/titleview.md) is non-`nil`, the system ignores this property.

> **Note**:  `NSToolbar` doesn’t support an attributed title when the system displays a navigation bar’s content in a toolbar for an app built with Mac Catalyst. For more information, see [`Display content in a toolbar on Mac`](uinavigationitem/title#Display-content-in-a-toolbar-on-Mac.md).

## See Also

- [var title: String?](uinavigationitem/title.md)
  The navigation item’s title that displays in the navigation bar.
- [var largeTitle: String?](uinavigationitem/largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/attributedtitle-25fxb)*