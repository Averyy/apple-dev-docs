# itemTitle(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the title of the item at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func itemTitle(at index: Int) -> String
```

```objc
- (NSString *) itemTitleAtIndex:(NSInteger) index;
```

#### Return Value

The title of the item, or an empty string if no item exists at the specified index.

## Parameters

- `index`: The index of the item you want.

## See Also

### Getting menu items
- [var menu: NSMenu?](./menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](./itemarray.md)
  The array of menu item objects associated with the button.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [var itemTitles: [String]](./itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemtitle(at:))*