# menu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu associated with the pop-up button.

**Availability**:
- macOS

## Declaration

```swift
var menu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * menu;
```

## Discussion

If another menu was already associated with the pop-up button, this method releases its reference to the old menu.

## See Also

### Getting menu items
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
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/menu)*