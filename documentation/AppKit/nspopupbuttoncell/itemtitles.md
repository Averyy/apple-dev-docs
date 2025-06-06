# itemTitles

**Framework**: AppKit  
**Kind**: property

An array of `NSString` objects containing the titles of every item in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var itemTitles: [String] { get }
```

#### Discussion

The titles appear in the order in which the items appear in the menu. If the menu contains separator items, the array contains an empty string (`@""`) for each separator item.

## See Also

- [func itemTitle(at: Int) -> String](nspopupbuttoncell/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var titleOfSelectedItem: String?](nspopupbuttoncell/titleofselecteditem.md)
  The title of the item last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/itemtitles)*