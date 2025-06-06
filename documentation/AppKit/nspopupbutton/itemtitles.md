# itemTitles

**Framework**: AppKit  
**Kind**: property

An array of strings corresponding to the titles of the items in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var itemTitles: [String] { get }
```

#### Discussion

This property contains an array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which contains the title of an item in the menu. The order of the titles in this array matches the order of the items in the menu. If the menu contains separator items, the array contains an empty string for each separator item.

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
- [func item(withTitle: String) -> NSMenuItem?](nspopupbutton/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbutton/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemtitles)*