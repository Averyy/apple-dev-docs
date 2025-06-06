# itemArray

**Framework**: AppKit  
**Kind**: property

An array of [`NSMenuItem`](nsmenuitem.md) objects that represent the items in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var itemArray: [NSMenuItem] { get }
```

## See Also

- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.
- [var numberOfItems: Int](nspopupbuttoncell/numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](nspopupbuttoncell/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](nspopupbuttoncell/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTag: Int) -> Int](nspopupbuttoncell/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbuttoncell/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbuttoncell/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](nspopupbuttoncell/item(at:).md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbuttoncell/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbuttoncell/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/itemarray)*