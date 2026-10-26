# largeTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

String to be used as the large title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var largeTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * largeTitle;
```

#### Discussion

When `nil`, the navigation bar will use the navigation item’s current title.

## See Also

### Configuring the title
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](./attributedtitle-25fxb.md)
  An attributed string that the system renders as the title in the navigation bar.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.
- [attributedTitle](./attributedtitle-9l8p2.md)
  An attributed string that is rendered as the title in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitle)*