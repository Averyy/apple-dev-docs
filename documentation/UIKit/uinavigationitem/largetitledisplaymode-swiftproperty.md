# largeTitleDisplayMode

**Framework**: UIKit  
**Kind**: property

The mode for displaying the title of the navigation bar.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode { get set }
```

#### Discussion

When large titles are available, this property controls how the navigation bar displays the navigation item’s title. The default value of this property is [`UINavigationItem.LargeTitleDisplayMode.automatic`](uinavigationitem/largetitledisplaymode-swift.enum/automatic.md), which causes the title to use the same styling as the previously displayed navigation item. You can change the value of this property to force the navigation bar to display a large title ([`UINavigationItem.LargeTitleDisplayMode.always`](uinavigationitem/largetitledisplaymode-swift.enum/always.md)) or a small title ([`UINavigationItem.LargeTitleDisplayMode.never`](uinavigationitem/largetitledisplaymode-swift.enum/never.md)) for this item.

If the [`prefersLargeTitles`](uinavigationbar/preferslargetitles.md) property of the navigation bar is [`false`](https://developer.apple.com/documentation/swift/false), this property has no effect and the navigation item’s title is always displayed as a small title.

## See Also

- [var title: String?](uinavigationitem/title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](uinavigationitem/attributedtitle-25fxb.md)
- [var largeTitle: String?](uinavigationitem/largetitle.md)
  String to be used as the large title.
- [UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.property)*