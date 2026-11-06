# titleAlignment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred alignment of the navigation bar’s title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+

## Declaration

```swift
var titleAlignment: UINavigationItem.TitleAlignment { get set }
```

```objc
@property (nonatomic, assign, readwrite) UINavigationItemTitleAlignment titleAlignment;
```

## Discussion

The navigation bar resolves the alignment of its title automatically based on context, and the navigation item’s style. Use this property to override the system default.

The alignment the bar actually used is reported by `UITraitCollection.navigationTitleAlignment`.

Defaults to `UINavigationItemTitleAlignmentAutomatic`.

## See Also

### Configuring the title
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](./attributedtitle-25fxb.md)
  An attributed string that the system renders as the title in the navigation bar.
- [var largeTitle: String?](./largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.
- [UINavigationItem.TitleAlignment](./titlealignment-swift.enum.md)
- [attributedTitle](./attributedtitle-9l8p2.md)
  An attributed string that is rendered as the title in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.property)*