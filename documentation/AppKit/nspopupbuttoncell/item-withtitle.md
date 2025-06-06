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

- [func itemTitle(at: Int) -> String](nspopupbuttoncell/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemArray: [NSMenuItem]](nspopupbuttoncell/itemarray.md)
  An array of [`NSMenuItem`](nsmenuitem.md) objects that represent the items in the menu.
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
- [var lastItem: NSMenuItem?](nspopupbuttoncell/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/item(withtitle:))*