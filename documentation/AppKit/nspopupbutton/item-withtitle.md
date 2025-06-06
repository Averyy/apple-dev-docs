# item(withTitle:)

**Framework**: AppKit  
**Kind**: method

Returns the menu item with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func item(withTitle title: String) -> NSMenuItem?
```

#### Return Value

The menu item, or `nil` if no item with the specified title exists in the menu.

## Parameters

- `title`: The title of the menu item you want.

## See Also

- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func selectItem(withTitle: String)](nspopupbutton/selectitem(withtitle:).md)
  Selects the item with the specified title.
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
- [var lastItem: NSMenuItem?](nspopupbutton/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/item(withtitle:))*