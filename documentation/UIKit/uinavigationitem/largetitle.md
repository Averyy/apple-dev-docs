# largeTitle

**Framework**: UIKit  
**Kind**: property

String to be used as the large title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
var largeTitle: String? { get set }
```

#### Discussion

When `nil`, the navigation bar will use the navigation item’s current title.

## See Also

- [var title: String?](uinavigationitem/title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](uinavigationitem/attributedtitle-25fxb.md)
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitle)*