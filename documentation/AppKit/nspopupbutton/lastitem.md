# lastItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The last item in the menu.

**Availability**:
- macOS

## Declaration

```swift
var lastItem: NSMenuItem? { get }
```

```objc
@property (strong, readonly, nullable) NSMenuItem * lastItem;
```

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
- [var itemTitles: [String]](./itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/lastitem)*