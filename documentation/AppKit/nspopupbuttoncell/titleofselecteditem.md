# titleOfSelectedItem

**Framework**: AppKit  
**Kind**: property

The title of the item last selected by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleOfSelectedItem: String? { get }
```

#### Discussion

The value of this property is the title of the selected menu item, or an empty string if no item is selected.

## See Also

- [func selectItem(withTitle: String)](nspopupbuttoncell/selectitem(withtitle:).md)
  Selects the item with the specified title.
- [func itemTitle(at: Int) -> String](nspopupbuttoncell/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](nspopupbuttoncell/itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/titleofselecteditem)*