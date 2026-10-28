# largeTitleDisplayMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The mode for displaying the title of the navigation bar.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode { get set }
```

```objc
@property (nonatomic, assign, readwrite) UINavigationItemLargeTitleDisplayMode largeTitleDisplayMode;
```

## Discussion

When large titles are available, this property controls how the navigation bar displays the navigation item’s title. The default value of this property is [`UINavigationItem.LargeTitleDisplayMode.automatic`](./largetitledisplaymode-swift.enum/automatic.md), which causes the title to use the same styling as the previously displayed navigation item. You can change the value of this property to force the navigation bar to display a large title ([`UINavigationItem.LargeTitleDisplayMode.always`](./largetitledisplaymode-swift.enum/always.md)) or a small title ([`UINavigationItem.LargeTitleDisplayMode.never`](./largetitledisplaymode-swift.enum/never.md)) for this item.

If the [`prefersLargeTitles`](../uinavigationbar/preferslargetitles.md) property of the navigation bar is [`false`](../../Swift/false.md), this property has no effect and the navigation item’s title is always displayed as a small title.

## See Also

### Configuring the title
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](./attributedtitle-25fxb.md)
  An attributed string that the system renders as the title in the navigation bar.
- [var largeTitle: String?](./largetitle.md)
  String to be used as the large title.
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.
- [attributedTitle](./attributedtitle-9l8p2.md)
  An attributed string that is rendered as the title in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.property)*