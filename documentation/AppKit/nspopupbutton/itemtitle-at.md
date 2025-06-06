# itemTitle(at:)

**Framework**: AppKit  
**Kind**: method

Returns the title of the item at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func itemTitle(at index: Int) -> String
```

#### Return Value

The title of the item, or an empty string if no item exists at the specified index.

## Parameters

- `index`: The index of the item you want.

## See Also

- [var menu: NSMenu?](nspopupbutton/menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](nspopupbutton/numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](nspopupbutton/itemarray.md)
  The array of menu item objects associated with the button.
- [func item(at: Int) -> NSMenuItem?](nspopupbutton/item(at:).md)
  Returns the menu item at the specified index.
- [var itemTitles: [String]](nspopupbutton/itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbutton/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbutton/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemtitle(at:))*