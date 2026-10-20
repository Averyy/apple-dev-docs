# itemTitles

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of strings corresponding to the titles of the items in the menu.

**Availability**:
- macOS

## Declaration

```swift
var itemTitles: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * itemTitles;
```

#### Discussion

This property contains an array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains the title of an item in the menu. The order of the titles in this array matches the order of the items in the menu. If the menu contains separator items, the array contains an empty string for each separator item.

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
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemtitles)*