# title

**Framework**: UIKit  
**Kind**: property

The navigation item’s title that displays in the navigation bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var title: String? { get set }
```

#### Discussion

The default value is `nil`.

When the navigation item is on the navigation item stack and is second from the top — in other words, its view controller manages the views that the user would navigate back to — the value in this property is used for the back button on the top-most navigation bar. If the value of this property is `nil`, the system uses the string “Back” as the text of the back button. In iOS 11 and later, the size and position of the title is determined by the [`prefersLargeTitles`](uinavigationbar/preferslargetitles.md) property of the navigation bar and the [`largeTitleDisplayMode`](uinavigationitem/largetitledisplaymode-swift.property.md) property of the navigation item.

## See Also

- [init(title: String)](uinavigationitem/init(title:).md)
  Creates a navigation item with the specified title.
- [var titleView: UIView?](uinavigationitem/titleview.md)
  A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [class UINavigationItem](uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/title)*