# itemArray

**Framework**: AppKit  
**Kind**: property

The array of menu item objects associated with the button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var itemArray: [NSMenuItem] { get }
```

#### Discussion

This property contains an array of [`NSMenuItem`](nsmenuitem.md) objects representing the items in the menu. Usually, you access menu items using the methods and properties of this class rather than accessing the items directly.

## See Also

- [func insertItem(withTitle: String, at: Int)](nspopupbutton/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(at: Int)](nspopupbutton/removeitem(at:).md)
  Removes the item at the specified index.
- [var menu: NSMenu?](nspopupbutton/menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](nspopupbutton/numberofitems.md)
  The number of items in the menu.
- [func item(at: Int) -> NSMenuItem?](nspopupbutton/item(at:).md)
  Returns the menu item at the specified index.
- [func itemTitle(at: Int) -> String](nspopupbutton/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](nspopupbutton/itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbutton/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbutton/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemarray)*