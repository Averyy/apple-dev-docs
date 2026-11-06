# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu item at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func item(at index: Int) -> NSMenuItem?
```

```objc
- (NSMenuItem *) itemAtIndex:(NSInteger) index;
```

## Return Value

The menu item at `index`.

## Discussion

This method throws an exception if you pass a negative `index`, including `-1`, or an `index` beyond the last item. Methods like [`indexOfItem(withTarget:andAction:)`](./indexofitem%28withtarget,andaction%29.md) return `-1` when no item matches, so check the index before you call this method.

## Parameters

- `index`: The index of the item you want. Pass the index of an existing menu item.

## See Also

### Getting menu items
- [var menu: NSMenu?](./menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](./itemarray.md)
  The array of menu item objects associated with the button.
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](./itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/item(at:))*