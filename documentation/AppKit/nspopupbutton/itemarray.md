# itemArray

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of menu item objects associated with the button.

**Availability**:
- macOS

## Declaration

```swift
var itemArray: [NSMenuItem] { get }
```

```objc
@property (copy, readonly) NSArray<NSMenuItem *> * itemArray;
```

## Discussion

This property contains an array of [`NSMenuItem`](../nsmenuitem.md) objects representing the items in the menu. Usually, you access menu items using the methods and properties of this class rather than accessing the items directly.

## See Also

### Related Documentation
- [func insertItem(withTitle: String, at: Int)](./insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index.
### Getting menu items
- [var menu: NSMenu?](./menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](./itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/itemarray)*