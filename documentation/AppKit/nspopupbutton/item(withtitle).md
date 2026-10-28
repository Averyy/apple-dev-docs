# item(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu item with the specified title.

**Availability**:
- macOS

## Declaration

```swift
func item(withTitle title: String) -> NSMenuItem?
```

```objc
- (NSMenuItem *) itemWithTitle:(NSString *) title;
```

## Return Value

The menu item, or `nil` if no item with the specified title exists in the menu.

## Parameters

- `title`: The title of the menu item you want.

## See Also

### Related Documentation
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func addItem(withTitle: String)](./additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
### Getting menu items
- [var menu: NSMenu?](./menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](./itemarray.md)
  The array of menu item objects associated with the button.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](./itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/item(withtitle:))*