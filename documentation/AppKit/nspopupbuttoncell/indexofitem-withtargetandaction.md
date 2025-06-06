# indexOfItem(withTarget:andAction:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the menu item with the specified target and action.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withTarget target: Any?, andAction actionSelector: Selector?) -> Int
```

#### Return Value

The index of the menu item, or `-1` if no menu item contains the specified target and action.

#### Discussion

If you specify `NULL` for the `actionSelector` parameter, the index of the first menu item with the specified target is returned.

The `NSPopUpButtonCell` class assigns a default action and target to each menu item, but you can change these values using the setAction: and setTarget: methods of [`NSMenuItem`](nsmenuitem.md).

## Parameters

- `target`: The target object associated with the menu item.
- `actionSelector`: The action method associated with the menu item.

## See Also

- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
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
- [func item(at: Int) -> NSMenuItem?](nspopupbuttoncell/item(at:).md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbuttoncell/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbuttoncell/lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofitem(withtarget:andaction:))*