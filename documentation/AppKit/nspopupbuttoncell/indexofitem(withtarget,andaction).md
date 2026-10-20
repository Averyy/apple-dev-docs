# indexOfItem(withTarget:andAction:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item with the specified target and action.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTarget target: Any?, andAction actionSelector: Selector?) -> Int
```

```objc
- (NSInteger) indexOfItemWithTarget:(id) target andAction:(SEL) actionSelector;
```

#### Return Value

The index of the menu item, or `-1` if no menu item contains the specified target and action.

#### Discussion

If you specify `NULL` for the `actionSelector` parameter, the index of the first menu item with the specified target is returned.

The `NSPopUpButtonCell` class assigns a default action and target to each menu item, but you can change these values using the setAction: and setTarget: methods of [`NSMenuItem`](../nsmenuitem.md).

## Parameters

- `target`: The target object associated with the menu item.
- `actionSelector`: The action method associated with the menu item.

## See Also

### Related Documentation
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
### Accessing the items
- [var itemArray: [NSMenuItem]](./itemarray.md)
  An array of [`NSMenuItem`](../nsmenuitem.md) objects that represent the items in the menu.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofitem(withtarget:andaction:))*