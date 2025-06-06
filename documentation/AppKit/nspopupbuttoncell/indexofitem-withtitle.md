# indexOfItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the item with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withTitle title: String) -> Int
```

#### Return Value

The index of the item or `-1` if no item with the specified title was found.

## Parameters

- `title`: The title of the item you want. You must not pass   for this parameter.

## See Also

- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [var itemArray: [NSMenuItem]](nspopupbuttoncell/itemarray.md)
  An array of [`NSMenuItem`](nsmenuitem.md) objects that represent the items in the menu.
- [var numberOfItems: Int](nspopupbuttoncell/numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](nspopupbuttoncell/index(of:).md)
  Returns the index of the specified menu item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofitem(withtitle:))*