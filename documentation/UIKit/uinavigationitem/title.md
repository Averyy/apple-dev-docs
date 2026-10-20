# title

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The navigation item’s title that displays in the navigation bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * title;
```

#### Discussion

The default value is `nil`.

When the navigation item is on the navigation item stack and is second from the top — in other words, its view controller manages the views that the user would navigate back to — the value in this property is used for the back button on the top-most navigation bar. If the value of this property is `nil`, the system uses the string “Back” as the text of the back button. In iOS 11 and later, the size and position of the title is determined by the [`prefersLargeTitles`](../uinavigationbar/preferslargetitles.md) property of the navigation bar and the [`largeTitleDisplayMode`](./largetitledisplaymode-swift.property.md) property of the navigation item.

##### Display content in a toolbar on Mac

For Mac apps built with Mac Catalyst, the system can display a navigation bar’s content in an [`NSToolbar`](../../AppKit/nstoolbar.md). When the system displays a navigation bar’s content in a toolbar, `title` and [`subtitle`](./subtitle.md) are only supported when you associate the navigation bar with the [`UINavigationBar.NSToolbarSection.content`](../uinavigationbar/nstoolbarsection/content.md) section of the toolbar. The system ignores values from all other sections. `NSToolbar` doesn’t support a navigation item’s [`titleView`](./titleview.md), large titles, or attributed titles, regardless of section.

For more information about when the system displays a navigation bar’s content in a toolbar, see [Building with Mac Catalyst](../uinavigationbar.md#Building-with-Mac-Catalyst).

When present, `title` and `subtitle` take precedence over the window scene’s [`title`](../uiscene/title.md) and [`subtitle`](../uiscene/subtitle.md). To avoid displaying an orphaned scene subtitle, the system only uses the scene’s subtitle when the navigation item hasn’t set a title. These values appear in the standard locations [`NSWindow`](../../AppKit/nswindow.md) uses, rather than above the navigation item’s column.

## See Also

### Related Documentation
- [init(title: String)](./init%28title%29.md)
  Creates a navigation item with the specified title.
- [var titleView: UIView?](./titleview.md)
  A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [class UINavigationItem](../uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
### Configuring the title
- [var attributedTitle: AttributedString?](./attributedtitle-25fxb.md)
  An attributed string that the system renders as the title in the navigation bar.
- [var largeTitle: String?](./largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/title)*