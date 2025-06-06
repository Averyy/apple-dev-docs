# lastItem

**Framework**: AppKit  
**Kind**: property

The last item in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var lastItem: NSMenuItem? { get }
```

## See Also

- [var menu: NSMenu?](nspopupbutton/menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](nspopupbutton/numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](nspopupbutton/itemarray.md)
  The array of menu item objects associated with the button.
- [func item(at: Int) -> NSMenuItem?](nspopupbutton/item(at:).md)
  Returns the menu item at the specified index.
- [func itemTitle(at: Int) -> String](nspopupbutton/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](nspopupbutton/itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbutton/item(withtitle:).md)
  Returns the menu item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/lastitem)*